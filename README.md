# InspiringPDFs


The chatbot allows users to upload a PDF, process the document, and ask questions about the content.

## Project Structure

- **main.py**: Entry point of the application.
- **data_preprocessing.py**: Handles PDF reading, text extraction, and chunking.
- **data_ingestion.py**: Manages vector database operations and data ingestion.
- **chat_pipeline.py**: Handles queries using chains, retrievers, memory, and compressors.

## Requirements

- Python 3.8+
- Streamlit
- PyPDF2
- LangChain
- FAISS
- OpenAI
- python-dotenv
- streamlit_extras

## Installation

1. Clone the repository.
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
    ```
3. Add .env file and place the OPENAI_API_KEY:
   ```sh
   OPENAI_API_KEY = sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
5. Run the application
    ```sh
    streamlit run src/main.py
    ```

## PDF CHAT ARCHITECTURE

![image](https://github.com/Chhabii/InspiringPDFs/assets/60286478/b914ce20-9a83-4a96-addd-bd94f013fbf5)

## LLM-Powered PDF Chat System Architecture with Langchain Memory and Compression

![Untitled-2024-05-01-1113](https://github.com/Chhabii/InspiringPDFs/assets/60286478/625103f7-221d-4942-9594-7b58b79470a1)


## Flow Explanation:
### 1. Upload and Data Extraction:

- The user uploads PDFs, which are processed to extract textual data.
### 2. Text Chunking and Embedding:

- Extracted text is split into chunks and embedded into vectors.
### 3. Vector Store and Compression:

- Embeddings are stored in a vector store. Compression techniques are applied to optimize storage.
### 4. Memory and Query Processing:

- Memory techniques store conversation context. The user's query is processed to retrieve relevant documents.
### 5. Context Building and Response Generation:

- Context is built from retrieved documents. The system generates responses using context and memory.
### 6. User Interaction and Chat History:

- The user interface displays chat history, showing the interactive conversation flow.

## Ouput 

![image](https://github.com/Chhabii/InspiringPDFs/assets/60286478/409d472f-5297-4cf4-9250-9679f1c742c3)

## Chat History

![image](https://github.com/Chhabii/InspiringPDFs/assets/60286478/58be46f6-3890-4c15-9270-dcdd93b8470c)

