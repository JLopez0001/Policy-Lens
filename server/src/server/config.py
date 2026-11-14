from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "policies"
    dimension: int = 768

    # Ollama
    ollama_url: str = "http://localhost:11434"
    ollama_llm_model: str = "llama3.2:3b"
    ollama_embed_model: str = "nomic-embed-text"

    # Chunking
    chunk_size: int = 1000
    chunk_overlap: int = 200

settings = Settings()