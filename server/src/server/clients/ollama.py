from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from server.config import settings

llm = Ollama(
    model= settings.ollama_llm_model,
    base_url= settings.ollama_url,
    request_timeout= 120.0
)

embed_model = OllamaEmbedding(
    model_name= settings.ollama_embed_model,
    base_url= settings.ollama_url
)