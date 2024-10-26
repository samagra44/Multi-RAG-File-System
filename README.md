# RAG Multi-File Chat Application

## Overview

The RAG Multi-File Chat Application is a web-based tool designed to facilitate interactive conversations with multiple documents. By leveraging Retrieval-Augmented Generation (RAG) techniques, the application allows users to upload various documents, which are then processed to enable intelligent querying. The application utilizes advanced language models and embeddings to provide contextually relevant responses based on the content of the uploaded files.

## Features

- **Multi-File Upload**: Users can select and upload multiple files simultaneously for processing.
- **Document Processing**: The application reads and extracts content from the uploaded documents, making it available for querying.
- **Conversational Interface**: Users can ask questions related to the content of the documents, and the application generates responses based on the information contained within.
- **Clear Functionality**: Users can easily reset the application, clearing all loaded documents and chat history.
- **Error Handling**: The application provides user-friendly error messages to guide users in case of issues during document loading or query processing.
- **Responsive Design**: The application is built using Gradio, ensuring a user-friendly interface that works well on various devices.

## Technologies Used

- **Gradio**: A Python library for creating user interfaces for machine learning models, enabling easy interaction with the application.
- **Llama Index**: A library for managing and querying document indices, allowing efficient retrieval of information from loaded documents.
- **Groq**: A state-of-the-art language model used for generating responses based on the context of the loaded documents.
- **Hugging Face**: A platform that provides pre-trained models and embeddings for natural language processing tasks.
- **Python**: The programming language used to develop the application, ensuring readability and maintainability.

## Project Structure

```
RAG-Multi-File-Chat-App/
│
├── app.py                  # Main application file
├── requirements.txt        # List of dependencies
├── .env-example            # Environment variables for API keys
└── README.md               # Project documentation
```

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samagra44/Multi-RAG-File-System.git
   cd Multi-RAG-File-System
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate       # On Mac/Linux use `source venv/bin/activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory of the project and add the following lines:
   ```plaintext
   GROQ_API_KEY=<your_groq_api_key>
   HF_TOKEN=<your_huggingface_token>
   ```

   Make sure to replace `<your_groq_api_key>` and `<your_huggingface_token>` with your actual API keys.

## Usage

1. **Run the application**:
   Open your terminal and execute the following command:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open your web browser and navigate to `http://localhost:7860` (or the URL provided in the terminal).

3. **Load Documents**:
   - Click on the "Select files to load" button to open a file dialog.
   - Select multiple documents (e.g., PDF, TXT, etc.) that you want to upload.
   - Click the "Load Documents" button to process the uploaded files. The application will read the content and prepare it for querying.

4. **Ask Questions**:
   - In the "Enter your question" textbox, type your question related to the content of the loaded documents.
   - Press Enter to submit your question. The application will generate a response based on the information contained in the documents.

5. **Clear All**:
   - Click the "Clear" button to reset the application. This will remove all loaded documents and clear the chat history.

## Error Handling

The application includes error handling mechanisms to provide feedback to users. Common error messages include:

- **No file selected**: Displayed when the user attempts to load documents without selecting any files.
- **No Documents found**: Shown when the selected files do not contain any readable content.
- **Error loading documents**: Indicates an issue during the document loading process, along with the specific error message.
- **Error processing query**: Displayed when there is an issue generating a response to the user's question.

## Output

<p align="center">
<img src="https://github.com/user-attachments/assets/27bff7f4-28c6-4429-b8ce-62d1c0c28b9f" width=700 height=300 alt="animated"/>
</p>

## Acknowledgments

- Thanks to the developers of Gradio, Llama Index, Groq, and Hugging Face for their amazing libraries and tools that made this project possible.

## Contact

For any questions or inquiries, please reach out to [samagra183@gmail.com].
