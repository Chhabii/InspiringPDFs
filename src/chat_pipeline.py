from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_community.docstore.in_memory import InMemoryDocstore

class ChatPipeline:
    def __init__(self, vectorstore, model="gpt-3.5-turbo"):
        self.vectorstore = vectorstore
        self.llm = ChatOpenAI(model=model,temperature=0)
        self.compressor = LLMChainExtractor.from_llm(self.llm)
        self.memory = ConversationBufferMemory(return_messages=True)

    def create_retriever(self):
        base_retriever = self.vectorstore.as_retriever()
        compression_retriever = ContextualCompressionRetriever(base_compressor=self.compressor, base_retriever=base_retriever,num_relevant_documents=3 )
        return compression_retriever

    def process_query(self, query):
        retriever = self.create_retriever()
        docs = retriever.get_relevant_documents(query)
        
        if docs:
            context = "\n".join([doc.page_content for doc in docs])
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", "You are an intelligent assistant that helps answer questions based on the provided context: \n\n{context}\n\n Additionally, suggest related questions the user might ask. If you don't know the answer, kindly prompt the user to ask a more specific question about the document."),
                    ("human", "{question}")
                ]
            )
            chain = prompt | self.llm
            memory_variables = self.memory.load_memory_variables({})
            response = chain.invoke({
                'context': context,
                'question': query,
                **memory_variables
            })

            self.memory.save_context({"question": query}, {"answer": response.content})
            return response.content
        else:
            return "No relevant information found."
