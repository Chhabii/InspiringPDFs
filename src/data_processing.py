from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DataPreprocessing:
    def __init__(self, pdf):
        self.pdf = pdf

    def read_pdf(self):
        pdf_reader = PdfReader(self.pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def extract_chunks(self, text, chunk_size=1000, chunk_overlap=100):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = text_splitter.split_text(text=text)
        return chunks
