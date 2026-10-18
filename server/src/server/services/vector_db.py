from server.database import qdrant
from server.config import settings

class QdrantStorage:
    def __init__(
            self,
            url=settings.qdrant_url,
            dim=settings.dimension
    ):
         

 