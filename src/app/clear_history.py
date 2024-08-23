# Neccessary imports
import streamlit as st

# Global constants
INITIAL_MESSAGE = {
    "role": "assistant",
    "content": "Provide a website link and ask me questions regarding it ...",
}


def clear_chat_history():
    """
    Clears the chat history by resetting the `messages` list in the session state.

    After calling this function, the chat history will be empty, and the initial message
    asking for a website link will be displayed.
    """
    try:
        # Reset the messages list in the session state
        st.session_state.messages = [INITIAL_MESSAGE]

    except AttributeError:
        # Handle the case where session_state does not have a 'messages' attribute
        st.error("Session state is not initialized properly.")
