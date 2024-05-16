import streamlit as st
from data_processing import DataPreprocessing
from data_ingestion import DataIngestion
from chat_pipeline import ChatPipeline
from dotenv import load_dotenv
import os

def main():
    st.title("InspiringDocs")
    # st.sidebar.title("InpiringDocs")
    st.sidebar.markdown(
        """
        # InpiringDocs :notebook:
        :rocket: This app is an LLM-powered chatbot built using:

        - [Streamlit](https://streamlit.io/): For creating the interactive web interface.

        - [OpenAI](https://openai.com/): For language models.

        - [LangChain](https://langchain.com/): For building the chatbot and handling document retrieval.

        - [FAISS](https://github.com/facebookresearch/faiss): For vector storage and similarity search.
        

        **Workflow:**:arrow_down:
        1. **Upload PDF**: Users upload a PDF document which is then read and processed.
        2. **Text Extraction and Chunking**: The text is extracted from the PDF and split into manageable chunks for better processing.
        3. **Data Ingestion**: The text chunks are embedded using OpenAI embeddings and stored in a FAISS vector store to enable efficient retrieval.
        4. **Query Processing**: Users can ask questions about the content of the PDF. The chatbot retrieves relevant information from the FAISS vector store and generates responses using OpenAI language models.

        This workflow ensures that users can interactively query PDF documents and receive relevant, accurate information.


        """
    )
    st.sidebar.write(":heart: Made by Chhabi Acharya.")
    load_dotenv()

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    st.header("Chat with PDFs")
    st.markdown("""---""")

    st.subheader("1. Upload PDF")
    pdf = st.file_uploader("Upload a PDF", type='pdf')
    if pdf is not None:
        data_preprocessor = DataPreprocessing(pdf)
        text = data_preprocessor.read_pdf()
        if not text:
            st.write("No text extracted from PDF.")
            return
        chunks = data_preprocessor.extract_chunks(text)
        st.success(f"Total chunks created: {len(chunks)}")

        store_name = pdf.name[:-4]
        data_ingestor = DataIngestion(store_name)
        vectorstore = data_ingestor.create_vectorstore(chunks)

        chat_pipeline = ChatPipeline(vectorstore)

        st.subheader("2. Ask Questions")

        query = st.text_input("Ask a question about your PDF file:")
        if query:
            response = chat_pipeline.process_query(query)
            st.session_state.chat_history.append((query, response))

    st.markdown("---")
    st.subheader("3. Chat History")
    if st.session_state.chat_history:
        for query, response in st.session_state.chat_history:
            st.markdown(f"**You:** {query}")
            st.markdown(f"**Bot:** {response}")
    else:
        st.info("Upload a PDF and ask a question to see the chat history.")


if __name__ == "__main__":
    main()
