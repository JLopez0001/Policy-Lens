from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter

reader = PDFReader()
splitter = SentenceSplitter()