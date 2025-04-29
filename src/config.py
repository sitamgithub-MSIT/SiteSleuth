import os
from dotenv import load_dotenv
from google import genai
from langchain_google_genai import HarmBlockThreshold, HarmCategory

# load environment variables
load_dotenv()
USER_AGENT = os.environ.get("USER_AGENT")
genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Model settings
embedding_model = "models/gemini-embedding-exp-03-07"
qa_model = "gemini-2.0-flash"

# Chroma db settings
CHROMA_INDEX_PATH = "./chroma_db"

# Decoding settings
temperature = 0.3
max_output_tokens = 2048
top_k = 40
top_p = 0.85

# Safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Langsmith tracing settings
LANGCHAIN_TRACING_V2 = os.environ.get("LANGCHAIN_TRACING_V2")
LANGCHAIN_ENDPOINT = os.environ.get("LANGCHAIN_ENDPOINT")
LANGCHAIN_API_KEY = os.environ.get("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.environ.get("LANGCHAIN_PROJECT")
