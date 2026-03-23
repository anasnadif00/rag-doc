"""Service layer for dataset ingestion."""

from app.core.config import Settings
from app.domain.schemas import IngestRequest, IngestResponse
from app.ingestion.dataset_loader import DatasetLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant


class IngestService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.dataset_loader = DatasetLoader(settings=settings)
        
        # Initialize chunking and embedding models once
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.embeddings = OpenAIEmbeddings(model=self.settings.embedding_model, api_key=self.settings.openai_api_key)

    def run(self, request: IngestRequest) -> IngestResponse:
        # Load source documents
        source_documents = self.dataset_loader.load_documents(limit=request.limit)
        
        if not source_documents:
            return IngestResponse(
                status="success",
                dataset_name=self.settings.dataset_name,
                dataset_language=self.settings.dataset_language,
                collection_name=self.settings.qdrant_collection,
                documents_loaded=0,
                documents_processed=0,
                chunks_created=0,
            )

        # Chunk documents
        lc_docs = []
        for doc in source_documents:
            metadata = {
                "doc_id": doc.doc_id,
                "title": doc.title,
                "source": doc.source,
                "language": doc.language,
            }
            if doc.category:
                metadata["category"] = doc.category
                
            chunks = self.text_splitter.split_text(doc.text)
            for chunk in chunks:
                lc_docs.append(Document(page_content=chunk, metadata=metadata))

        # Store in Qdrant
        Qdrant.from_documents(
            lc_docs,
            self.embeddings,
            url=self.settings.qdrant_url,
            collection_name=self.settings.qdrant_collection,
            force_recreate=request.recreate_collection
        )

        return IngestResponse(
            status="success",
            dataset_name=self.settings.dataset_name,
            dataset_language=self.settings.dataset_language,
            collection_name=self.settings.qdrant_collection,
            documents_loaded=len(source_documents),
            documents_processed=len(source_documents),
            chunks_created=len(lc_docs),
        )
