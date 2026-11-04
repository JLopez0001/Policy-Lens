from server.database import qdrant
from server.config import settings
from qdrant_client.models import Distance, VectorParams, PointStruct

class QdrantStorage:
    """Stores and searches document embeddings in a Qdrant collection."""

    def __init__(
            self,
            collection: str =settings.qdrant_collection,
            dim: int =settings.dimension
    ) -> None:
        self.client = qdrant
        self.collection: str = collection

        # Create the collection on first run; dim must match the embedding model.
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
        
        """Insert or update points. Existing IDs are overwritten."""
        points=[
            PointStruct(id=ids[i], payload=payloads[i], vector=vectors[i])
            for i in range(len(ids))
        ]
        
        self.client.upsert(collection_name=self.collection, points=points)

    def search(self, vector_query: list[float], top_k: int = 5):
        results = self.client.query_points(
            collection_name= self.collection,
            query= vector_query,
            with_payload= True,
            limit= top_k
        ).points

        findings = []
        for r in results:
            payload = r.payload or {}
            findings.append(
                {
                   "text": payload.get("text", ""),
                   "sources": payload.get("sources", ""),
                   "score": r.score
                }
            )

        return findings