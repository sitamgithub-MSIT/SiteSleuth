# Necessary imports
import sys
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Local imports
from src.config import CHROMA_INDEX_PATH, embedding_model
from src.utils.chain import get_conversational_chain
from src.logger import logging
from src.exception import CustomExceptionHandling


def user_input(user_question: str) -> str:
    """
    Process user input and generate a response using conversational AI.

    Args:
        user_question (str): The question asked by the user.

    Returns:
        str: The generated response from the conversational AI model.

    Raises:
        Exception: Propagates exceptions from underlying operations, including loading models and generating responses.
    """

    try:
        # Create the embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model)

        # Load the Chroma index and get the similar documents
        new_db = Chroma(
            persist_directory=CHROMA_INDEX_PATH, embedding_function=embeddings
        )
        docs = new_db.similarity_search(user_question)

        # Get the conversational chain
        chain = get_conversational_chain()

        # Get the response from the chain
        response = chain.invoke(
            {"input_documents": docs, "question": user_question},
            return_only_outputs=True,
        )

        # Log the successful response generation
        logging.info("Response generated successfully.")

        # Return the response
        return response

    # Handle exceptions
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
