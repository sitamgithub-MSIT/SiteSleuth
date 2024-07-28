# SiteSleuth

This project empowers users to get the most out of any website by analyzing its content and answering questions based on the information found. SiteSleuth utilizes an Artificial Conversational Entity powered by the Gemini API.

## Project Structure

The project is structured as follows:

- `assets`: This directory contains the output responses screenshots.

- `src`: This directory contains the source code for the project.

  - `app`: This directory contains the code for actual model response generation.

    - `clear_history.py`: This file contains the code for clearing the chat history.
    - `response.py`: This file contains the code for the chatbot response generation.

  - `utils`: This directory contains the utility functions for the project.

    - `chain.py`: This file contains the conversation chain implementation.
    - `data_loader.py`: This file contains the code for loading the website data.
    - `embeddings.py`: This file contains the code for the embeddings generation.
    - `text_processing.py`: This file contains the code for further text processing like text splitting, chunking, etc.

  - `config.py`: This file contains the configuration for the Gemini API.
  - `exception.py`: This file contains the exception handling for the project.
  - `logger.py`: This file contains the logging configuration for the project.

- `app.py`: This file contains the code for the Streamlit application.
- `Dockerfile`: This file contains the Docker configuration for the project.
- `.dockerignore`: This file contains the files to be ignored by Docker.
- `.gitignore`: This file contains the files to be ignored by Git.
- `.gcloudignore`: This file contains the files to be ignored by Google Cloud.
- `.env.example`: This file contains the environment variables required for the project.
- `requirements.txt`: This file contains the required dependencies for the project.
- `README.md`: This file contains the project documentation.
- `LICENSE`: This file contains the project license.

## Tech Stack

- Python: Python is used as the primary programming language for this project.
- Gemini API: These APIs provide advanced natural language processing and computer vision capabilities.
- Langchain: Langchain is used for the RAG (Retrieval Augmented Generation) implementation.
- Chroma DB: Chroma DB is used as the vector store for the embeddings.
- Streamlit: Streamlit is used for building interactive UIs for the chat interface.
- Hugging Face Spaces: Hugging Face spaces is used for deployment of the streamlit application.
- Docker: Docker is used to containerize the application.
- Cloud Run: Google Cloud Run is used to deploy the containerized application.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/SiteSleuth.git`
2. Change the directory: `cd SiteSleuth`
3. Create a virtual environment: `python -m venv tutorial-env`
4. Activate the virtual environment: `tutorial-env\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the Gradio application: `streamlit run app.py`

Now, open up your local host and you should see the web application running. For more information, refer to the Streamlit documentation [here](https://docs.streamlit.io/). Also, a live version of the application can be found [here](https://sitammeur-sitesleuth.hf.space/) in the Hugging Face Spaces.

## Usage

Once the application is up and running, you can interact with the conversational entity through the provided UI. It can analyze the content of websites and answer your questions based on the information found.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
