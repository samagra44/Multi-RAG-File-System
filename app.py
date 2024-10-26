import gradio as gr
import os
import asyncio
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.groq import Groq
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()
index = None
query_engine = None

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = Groq(
    model="llama3-8b-8192",
    api_key=GROQ_API_KEY
)

Settings.llm = llm
embedd_model = HuggingFaceEndpointEmbeddings(huggingfacehub_api_token=os.getenv("HF_TOKEN"))

def load_documents(file_objs):
    global index, query_engine
    try:
        if not file_objs:
            return "No file selected"
        documents = []
        documents_name = []
        for file_obj in file_objs:
            documents_name.append(file_obj.name)
            loaded_docs = SimpleDirectoryReader(input_files=[file_obj.name]).load_data()
            documents.extend(loaded_docs)
        if not documents:
            return "No Documents found in the selected files"
        index = VectorStoreIndex.from_documents(
            documents=documents,
            llm=llm,
            embed_model=embedd_model
        )
        query_engine = index.as_query_engine()
        return f"Successfully loaded {len(documents)} documents from the files: {', '.join(documents_name)}"
    except Exception as e:
        return f"Error loading documents: {str(e)}"

async def perform_rag(query, history):
    global query_engine
    if query_engine is None:
        return history + [("Please load documents first.", None)]
    try:
        response = await asyncio.to_thread(query_engine.query, query)
        return history + [(query, str(response))]
    except Exception as e:
        return history + [(query, f"Error processing query: {str(e)}")]

def clear_all():
    global index, query_engine
    index = None
    query_engine = None
    return None, "", [], ""

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# RAG Multi-File Chat Application")
    with gr.Row():
        file_input = gr.File(label="Select files to load", file_count="multiple")
        load_btn = gr.Button("Load Documents")
    load_output = gr.Textbox(label="Load Status")
    msg = gr.Textbox("Enter your question")
    chatbot = gr.Chatbot()
    clear = gr.Button("Clear")

    load_btn.click(load_documents, inputs=[file_input], outputs=[load_output])
    msg.submit(perform_rag, inputs=[msg, chatbot], outputs=[chatbot])
    clear.click(clear_all, outputs=[file_input, load_output, chatbot, msg], queue=False)

if __name__ == "__main__":
    demo.queue()
    demo.launch(share=True)