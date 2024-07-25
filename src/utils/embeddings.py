# Langchain imports
import sys
from typing import List
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Local imports
from src.config import CHROMA_INDEX_PATH, embedding_model
from src.logger import logging
from src.exception import CustomExceptionHandling


# Get the embeddings from chunks
def get_vector_store(chunks: List[str]):
    """
    Creates a vector store using FAISS from a list of chunks.

    Args:
        chunks (List[str]): A list of chunks to be used for creating the vector store.

    Returns:
        Chroma vector store: The created vector store.
    """

    try:
        # Create the embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model)

        # Create the vector store using Chroma
        vector_store = Chroma.from_documents(
            chunks, embeddings, persist_directory=CHROMA_INDEX_PATH
        )
        logging.info("Vector store created and saved successfully.")

        # Return the vector store
        return vector_store

    # Handle exceptions that may occur during vector store creation
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
