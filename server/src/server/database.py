from qdrant_client import QdrantClient
from server.config import settings

qdrant = QdrantClient(url=settings.qdrant_url)