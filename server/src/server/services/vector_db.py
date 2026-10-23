from server.database import qdrant
from server.config import settings
from qdrant_client.models import Distance, VectorParams, PointStruct

class QdrantStorage:
    def __init__(
            self,
            collection: str =settings.qdrant_collection,
            dim: int =settings.dimension
    ) -> None:
        self.client = qdrant
        self.collection: str = collection

        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection, 
                vectors_config= VectorParams(size=dim, distance=Distance.COSINE)
            )

    def upsert(
            self, 
            ids:list[int | str], 
            vectors:list[list[float]], 
            payloads: list[dict]
        ) -> None:

        points=[
            PointStruct(id=ids[i], payload=payloads[i], vector=vectors[i])
            for i in range(len(ids))
        ]
        
        self.client.upsert(collection_name=self.collection, points=points)
        
    

 