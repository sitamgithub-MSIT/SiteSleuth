# Necessary imports
import sys
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


# Make chunks out of the document
def get_document_chunks(document: str) -> List[str]:
    """
    Splits a document into chunks using a RecursiveCharacterTextSplitter.

    Args:
        document (str): The document to be split.

    Returns:
        List[str]: A list of strings representing the chunks of the document.
    """

    try:
        # Split the document into chunks using the RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, add_start_index=True
        )
        chunks = splitter.split_documents(document)

        # Log the successful document splitting
        logging.info("Document split into chunks successfully.")

        # Return the chunks
        return chunks

    # Handle exceptions that may occur during document splitting
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
