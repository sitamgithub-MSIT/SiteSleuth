# Neccessary imports
import warnings

warnings.filterwarnings("ignore")
import streamlit as st

# Local imports
from src.utils.data_loader import get_web_document
from src.utils.text_processing import get_document_chunks
from src.utils.embeddings import get_vector_store

from src.app.clear_history import clear_chat_history
from src.app.response import user_input


# Main function to run the SiteSleuth application
def main():
    """
    The main function of the SiteSleuth application.

    This function sets up the page configuration, handles user input, and displays chat messages and bot responses.
    """
    # Set the page configuration
    st.set_page_config(page_title="SiteSleuth", page_icon="🌐")

    # Sidebar for uploading website link
    with st.sidebar:
        st.title("Menu: ")
        website_url = st.text_input(
            "Provide a website link and Click on the Submit & Process Button 🔗"
        )

        # Check if the website URL is valid and start processing
        if website_url and website_url.startswith("https://"):
            if st.button("Submit & Process ✅"):
                with st.spinner("Processing..."):
                    raw_document = get_web_document(website_url)
                    text_chunks = get_document_chunks(raw_document)
                    get_vector_store(text_chunks)
                    st.success("Done")

        # Display a warning message if the website URL is invalid
        elif st.button("Submit & Process ✅"):
            st.warning("Please provide a valid website link")

    # Main content area for displaying chat messages
    st.title("SiteSleuth🌐 - Chat with Websites")
    st.subheader(
        "Welcome to SiteSleuth! 🌟 SiteSleuth is a conversational AI that can answer questions based on the context of a website."
    )
    st.text(
        "🚀 Provide a website link and start your interactive chat session with SiteSleuth🌐"
    )
    st.sidebar.button("Clear Chat History 🔄", on_click=clear_chat_history)

    # Chat input
    # Placeholder for chat messages
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Provide a website link and ask me questions regarding it ...",
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Display chat messages and bot response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = user_input(prompt)
                placeholder = st.empty()
                full_response = ""
                for item in response["output_text"]:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        if response is not None:
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)


# Run the application
if __name__ == "__main__":
    main()
