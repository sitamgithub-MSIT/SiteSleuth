# Necessary imports
import sys
from typing import Optional
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from requests.exceptions import SSLError

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
        # If the website URL ends with ".pdf", load the document using PyPDFLoader
        if website_url.endswith(".pdf"):
            loader = PyPDFLoader(website_url, extract_images=True)

        # Otherwise, load the document using WebBaseLoader
        else:
            try:
                # Attempt to load the document with SSL verification
                loader = WebBaseLoader(website_url, verify_ssl=True)
                document = loader.load()

                # Log the successful document loading with SSL verification
                logging.info("Document loaded successfully with SSL verification.")

            # Handle SSL verification failure
            except SSLError as ssl_error:
                # Log the SSL verification failure
                logging.warning(
                    f"SSL verification failed for {website_url}: {ssl_error}"
                )

                try:
                    # Fallback to loading without SSL verification
                    loader = WebBaseLoader(website_url, verify_ssl=False)
                    document = loader.load()

                    # Log the successful document loading without SSL verification
                    logging.info(
                        "Document loaded successfully without SSL verification."
                    )

                # Handle any other exceptions that may occur
                except Exception as e:
                    raise CustomExceptionHandling(e, sys) from e

        # Return the document
        return document

    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
