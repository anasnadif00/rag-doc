"""Small async key-value abstractions used by auth and chat state."""

from __future__ import annotations

import asyncio
import json
import time
from collections import defaultdict
from typing import Any

from redis.asyncio import Redis

from app.core.config import Settings


class AsyncStateStore:
    async def set_json(self, key: str, value: dict[str, Any], ttl_seconds: int) -> None:
        raise NotImplementedError

    async def get_json(self, key: str) -> dict[str, Any] | None:
        raise NotImplementedError

    async def pop_json(self, key: str) -> dict[str, Any] | None:
        raise NotImplementedError

    async def increment(self, key: str, ttl_seconds: int, amount: int = 1) -> int:
        raise NotImplementedError

    async def append_list(self, key: str, value: dict[str, Any], ttl_seconds: int, trim_to: int) -> None:
        raise NotImplementedError

    async def read_list(self, key: str) -> list[dict[str, Any]]:
        raise NotImplementedError

    async def delete(self, key: str) -> None:
        raise NotImplementedError


class RedisStateStore(AsyncStateStore):
    def __init__(self, redis: Redis, namespace: str) -> None:
        self.redis = redis
        self.namespace = namespace

    def _key(self, key: str) -> str:
        return f"{self.namespace}:{key}"

    async def set_json(self, key: str, value: dict[str, Any], ttl_seconds: int) -> None:
        await self.redis.set(self._key(key), json.dumps(value), ex=ttl_seconds)

    async def get_json(self, key: str) -> dict[str, Any] | None:
        raw = await self.redis.get(self._key(key))
        if raw is None:
            return None
        return json.loads(raw)

    async def pop_json(self, key: str) -> dict[str, Any] | None:
        namespaced = self._key(key)
        async with self.redis.pipeline(transaction=True) as pipe:
            pipe.get(namespaced)
            pipe.delete(namespaced)
            raw, _ = await pipe.execute()
        if raw is None:
            return None
        return json.loads(raw)

    async def increment(self, key: str, ttl_seconds: int, amount: int = 1) -> int:
        namespaced = self._key(key)
        async with self.redis.pipeline(transaction=True) as pipe:
            pipe.incrby(namespaced, amount)
            pipe.expire(namespaced, ttl_seconds)
            value, _ = await pipe.execute()
        return int(value)

    async def append_list(self, key: str, value: dict[str, Any], ttl_seconds: int, trim_to: int) -> None:
        namespaced = self._key(key)
        async with self.redis.pipeline(transaction=True) as pipe:
            pipe.rpush(namespaced, json.dumps(value))
            pipe.ltrim(namespaced, -trim_to, -1)
            pipe.expire(namespaced, ttl_seconds)
            await pipe.execute()

    async def read_list(self, key: str) -> list[dict[str, Any]]:
        items = await self.redis.lrange(self._key(key), 0, -1)
        return [json.loads(item) for item in items]

    async def delete(self, key: str) -> None:
        await self.redis.delete(self._key(key))


class InMemoryStateStore(AsyncStateStore):
    def __init__(self, namespace: str) -> None:
        self.namespace = namespace
        self._lock = asyncio.Lock()
        self._values: dict[str, tuple[float | None, str]] = {}
        self._lists: defaultdict[str, list[tuple[float | None, str]]] = defaultdict(list)

    def _key(self, key: str) -> str:
        return f"{self.namespace}:{key}"

    def _now(self) -> float:
        return time.time()

    def _cleanup_key(self, key: str) -> None:
        item = self._values.get(key)
        if item and item[0] is not None and item[0] <= self._now():
            self._values.pop(key, None)
        list_items = self._lists.get(key)
        if not list_items:
            return
        self._lists[key] = [
            (expires_at, payload)
            for expires_at, payload in list_items
            if expires_at is None or expires_at > self._now()
        ]
        if not self._lists[key]:
            self._lists.pop(key, None)

    def _expires_at(self, ttl_seconds: int) -> float | None:
        if ttl_seconds <= 0:
            return None
        return self._now() + ttl_seconds

    async def set_json(self, key: str, value: dict[str, Any], ttl_seconds: int) -> None:
        async with self._lock:
            namespaced = self._key(key)
            self._values[namespaced] = (self._expires_at(ttl_seconds), json.dumps(value))

    async def get_json(self, key: str) -> dict[str, Any] | None:
        async with self._lock:
            namespaced = self._key(key)
            self._cleanup_key(namespaced)
            item = self._values.get(namespaced)
            if item is None:
                return None
            return json.loads(item[1])

    async def pop_json(self, key: str) -> dict[str, Any] | None:
        async with self._lock:
            namespaced = self._key(key)
            self._cleanup_key(namespaced)
            item = self._values.pop(namespaced, None)
            if item is None:
                return None
            return json.loads(item[1])

    async def increment(self, key: str, ttl_seconds: int, amount: int = 1) -> int:
        async with self._lock:
            namespaced = self._key(key)
            self._cleanup_key(namespaced)
            item = self._values.get(namespaced)
            current = 0
            if item is not None:
                current = int(json.loads(item[1]))
            current += amount
            self._values[namespaced] = (self._expires_at(ttl_seconds), json.dumps(current))
            return current

    async def append_list(self, key: str, value: dict[str, Any], ttl_seconds: int, trim_to: int) -> None:
        async with self._lock:
            namespaced = self._key(key)
            self._cleanup_key(namespaced)
            values = self._lists[namespaced]
            values.append((self._expires_at(ttl_seconds), json.dumps(value)))
            if trim_to > 0 and len(values) > trim_to:
                del values[:-trim_to]

    async def read_list(self, key: str) -> list[dict[str, Any]]:
        async with self._lock:
            namespaced = self._key(key)
            self._cleanup_key(namespaced)
            return [json.loads(item[1]) for item in self._lists.get(namespaced, [])]

    async def delete(self, key: str) -> None:
        async with self._lock:
            namespaced = self._key(key)
            self._values.pop(namespaced, None)
            self._lists.pop(namespaced, None)


_in_memory_stores: dict[str, InMemoryStateStore] = {}
_redis_clients: dict[str, Redis] = {}


def get_state_store(settings: Settings) -> AsyncStateStore:
    if settings.redis_url.startswith("memory://"):
        store = _in_memory_stores.get(settings.redis_url)
        if store is None:
            store = InMemoryStateStore(namespace=settings.redis_namespace)
            _in_memory_stores[settings.redis_url] = store
        return store

    client = _redis_clients.get(settings.redis_url)
    if client is None:
        client = Redis.from_url(settings.redis_url, decode_responses=True)
        _redis_clients[settings.redis_url] = client
    return RedisStateStore(redis=client, namespace=settings.redis_namespace)
