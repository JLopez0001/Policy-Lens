from server.database import qdrant
from server.config import settings

class QdrantStorage:
    def __init__(
            self,
            collection=settings.qdrant_collection
            dim=settings.dimension
    ):
        self.client = qdrant
        self.collection = collection

 