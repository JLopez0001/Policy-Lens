from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "policies"

settings = Settings()