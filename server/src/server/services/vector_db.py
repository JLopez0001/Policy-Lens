from server.database import qdrant
from server.config import settings

class QdrantStorage:
    def __init__(
            self,
            collection: str =settings.qdrant_collection,
            dim: int =settings.dimension
    ):
        self.client = qdrant
        self.collection = collection

 