"""
Insert all methodes, you need for rag-support into this file
"""

from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders import (
    WebBaseLoader, 
    PyPDFLoader, 
    Docx2txtLoader,
)

from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

dotenv.load_dotenv()

os.environ["USER_AGENT"] = "myagent"
DB_DOCS_LIMIT = 10

# Function to stream the response of the LLM 
def stream_llm_response(llm_stream, messages):
    """this method is used for streaming the llm-response. 
    Do not forget to use the `yield` keyword instead of return
    """
    

# --- Indexing Phase ---

def load_doc_to_db():
    # Use loader according to doc type
    

def load_url_to_db():
   

def initialize_vector_db(docs):
    
   


def _split_and_load_docs(docs):
   

# --- Retrieval Augmented Generation (RAG) Phase ---

def _get_context_retriever_chain(vector_db, llm):
    

def get_conversational_rag_chain(llm):
  

def stream_llm_rag_response(llm_stream, messages):
   