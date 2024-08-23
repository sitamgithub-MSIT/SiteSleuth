# Necessary imports
import sys
import google.generativeai as genai
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling

# Model configuration
from src.config import (
    qa_model,
    temperature,
    top_k,
    top_p,
    safety_settings,
    max_output_tokens,
)


def get_conversational_chain():
    """
    Retrieves a conversational chain for answering questions based on the provided context and question.

    Returns:
        The conversational chain object.
    """
    # Define the prompt template
    prompt_template = """
    You are an intelligent web analysis assistant. Your task is to help users by answering their questions based on the content of a provided website. You should provide detailed and accurate answers based solely on the information available in the given context. If the answer is not available in the context, respond with, "The answer is not available in the provided context." Do not attempt to fabricate or guess answers.

    Instructions:
    1. Carefully analyze the context provided.
    2. Respond to the question clearly and descriptively.
    3. Ensure your response is detailed and relevant to the question asked.
    4. Maintain a polite and professional tone throughout the interaction.

    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    try:
        # Create the conversational chain
        model = ChatGoogleGenerativeAI(
            model=qa_model,
            client=genai,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            safety_settings=safety_settings,
            max_output_tokens=max_output_tokens,
        )

        # Define the prompt template
        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        # Load the QA chain with the specified model and prompt template
        chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)

        # Log the successful creation of the conversational chain
        logging.info("Successfully created conversational chain.")

        # Return the conversational chain
        return chain

    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
