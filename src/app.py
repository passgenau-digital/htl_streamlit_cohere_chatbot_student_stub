from langchain_cohere import ChatCohere
import streamlit as st
import os
import dotenv
import uuid
import sys
sys.path.append('src')

# check if it's linux so it works on Streamlit Cloud
# if os.name == 'posix':
#     __import__('pysqlite3')
#     import sys
#     sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain.schema import HumanMessage, AIMessage

from rag.rag_methods import (
    load_doc_to_db, 
    load_url_to_db,
    stream_llm_response,
    stream_llm_rag_response,
)

dotenv.load_dotenv()

MODELS = [    
    "cohere/command-r7b-12-2024",
    "cohere/command-r-plus-08-2024"
]


st.set_page_config(
    page_title="RAG LLM app", 
    page_icon="📚", 
    layout="centered", 
    initial_sidebar_state="expanded"
)


# --- Header ---
st.html("""<h2 style="text-align: center;">📚🔍 <i> RAG-based LLM Chatbot </i> 🤖💬</h2>""")


# --- Initial Setup ---
# check if there is a session id already stored
# initialize session variables
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "rag_sources" not in st.session_state:
    pass

if "messages" not in st.session_state:
   pass

# --- Side Bar LLM API Tokens ---
with st.sidebar:   
    # check if the user provided an api key for cohere model
    # either from system environment or via input box
    

# --- Main Content ---
# Checking if the user has introduced the Cohere API Key, if not, a warning is displayed


# if there is an api key, display all the elements needed for rag inside the sidebar

    
    # Main chat app
    # display input box for user prompt and system response!

