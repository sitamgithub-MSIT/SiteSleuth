# Necessary imports
import sys
from typing import Optional
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


def get_web_document(website_url: str) -> Optional[str]:
    """
    Retrieves the web document from the specified website URL.

    Args:
        website_url: The URL of the website to retrieve the document from.

    Returns:
        The web document retrieved from the website URL, or None if the website URL is empty or an error occurs.
    """

    # Check if the website URL is empty
    if not website_url:
        logging.warning("Empty website URL provided.")
        return None

    try:
        # Load the document from the website URL
        if website_url.endswith(".pdf"):
            loader = PyPDFLoader(website_url, extract_images=True)

        # Load the document using the WebBaseLoader
        else:
            loader = WebBaseLoader(website_url)

        # Load the document
        document = loader.load()

        # Log the successful document loading
        logging.info("Document loaded successfully.")

        # Return the document
        return document

    # Handle exceptions that may occur during document loading
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
