from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter

reader = PDFReader()
splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path:str):
    docs = reader.load_data(path)
    text = [d.text for d in docs if getattr(d, "text", None)]
    chuncks = []
    for t in text:
        chuncks.extend(splitter.split_text(t))
    return chuncks