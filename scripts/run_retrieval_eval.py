import argparse
import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.core.config import get_settings
from app.evaluation import build_lexical_index, clone_settings, run_retrieval_eval


def main() -> None:
    parser = argparse.ArgumentParser(description="Run deterministic retrieval evaluation over a curated KB fixture.")
    parser.add_argument(
        "--knowledge-base",
        type=str,
        default=str(Path("evals/fixtures/knowledge_base")),
        help="Knowledge base directory to evaluate.",
    )
    parser.add_argument(
        "--cases",
        type=str,
        default=str(Path("evals/retrieval_cases.json")),
        help="JSON file containing evaluation cases.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of retrieved chunks considered for hit@k.",
    )
    args = parser.parse_args()

    base_settings = get_settings()
    with TemporaryDirectory() as temp_dir:
        lexical_index_path = Path(temp_dir) / "lexical_index.json"
        settings = clone_settings(
            base_settings,
            knowledge_base_path=str(Path(args.knowledge_base).resolve()),
            lexical_index_path=str(lexical_index_path.resolve()),
            top_k=args.top_k,
        )
        chunks_created = build_lexical_index(settings)
        summary = run_retrieval_eval(settings=settings, cases_path=args.cases, top_k=args.top_k)
        summary["knowledge_base_path"] = settings.knowledge_base_path
        summary["lexical_index_path"] = settings.lexical_index_path
        summary["chunks_created"] = chunks_created
        print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
