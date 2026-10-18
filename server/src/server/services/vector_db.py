from server.database import qdrant
from server.config import settings

class QdrantStorage:
    def __init__(
            self,
            dim=settings.dimension
    ):
         
        self.client = qdrant

 