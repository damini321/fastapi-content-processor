# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services import process_url_content, process_pdf_content, generate_embeddings, search_query
import uuid
from .models import ChatRequest

app = FastAPI()

data_storage = {}  # Dictionary to store scraped/processed data

# 1. Process Web URL API
@app.post("/process_url")
async def process_url(url: str):
    try:
        content = process_url_content(url)
        chat_id = str(uuid.uuid4())  # Generate a unique chat_id
        data_storage[chat_id] = content
        return {"chat_id": chat_id, "message": "URL content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Process PDF Document API
@app.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        content = await process_pdf_content(file)
        chat_id = str(uuid.uuid4())  # Generate a unique chat_id
        data_storage[chat_id] = content
        return {"chat_id": chat_id, "message": "PDF content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Chat API
@app.post("/chat")
async def chat(request: ChatRequest):
    chat_id = request.chat_id
    question = request.question
    if chat_id not in data_storage:
        raise HTTPException(status_code=404, detail="Chat ID not found.")
    
    content = data_storage[chat_id]
    response = search_query(content, question)
    return {"response": response}
