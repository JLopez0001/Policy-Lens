from dataclasses import dataclass
from pathlib import Path
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from server.config import settings

reader = PDFReader()

splitter = SentenceSplitter(
    chunk_size=settings.chunk_size,        
    chunk_overlap=settings.chunk_overlap,
)

@dataclass
class Chunk:
    text: str   
    source: str 
    page: str   
    index: int  

def load_pdf(path: str):
    return reader.load_data(Path(path))

def chunk_documents(docs, source: str) -> list[Chunk]:
    chunks: list[Chunk] = []

    for doc in docs:
        text = getattr(doc, "text", "") or ""
        if not text.strip():
            continue

        page = str(doc.metadata.get("page_label", ""))
        for piece in splitter.split_text(text):
            chunks.append(
                Chunk(text=piece, source=source, page=page, index=len(chunks))
            )

    return chunks

def load_and_chunk_pdf(path: str) -> list[Chunk]:
    docs = load_pdf(path)
    return chunk_documents(docs, source=Path(path).name)
