# from langchain.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss
import os

class DataIngestion:
    def __init__(self, store_name):
        self.index_folder = f'src/faiss_store/{store_name}'
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions= 1024)

    def create_vectorstore(self, chunks):
        if os.path.exists(self.index_folder):
            try:
                vectorstore = FAISS.load_local(self.index_folder, self.embeddings, allow_dangerous_deserialization=True)
            except Exception as e:
                raise RuntimeError(f"Failed to load local storage: {e}")
        else:
            try:
                embedding_dim = len(self.embeddings.embed_documents(["test"])[0])
                faiss_index = faiss.IndexFlatL2(embedding_dim)
                docstore = InMemoryDocstore()
                index_to_docstore_id = {}
                vectorstore = FAISS(embedding_function=self.embeddings, index=faiss_index, docstore=docstore, index_to_docstore_id=index_to_docstore_id)
                chunk_embeddings = self.embeddings.embed_documents(chunks)
                vectorstore.add_embeddings(list(zip(chunks, chunk_embeddings)))
                vectorstore.save_local(self.index_folder)
            except Exception as e:
                raise RuntimeError(f"Failed to save local storage: {e}")
        return vectorstore
