# FastAPI Content Processor

This project is a backend service built using FastAPI that provides three main APIs for processing web content, PDF documents, and querying the processed content using a chat interface.

## Features

1. **Process Web URL API:**
   - Scrapes content from a given URL and stores it.
   - Returns a unique chat ID and a success message.

2. **Process PDF Document API:**
   - Extracts text from an uploaded PDF document and stores it.
   - Returns a unique chat ID and a success message.

3. **Chat API:**
   - Allows users to query the processed content (either from a URL or a PDF) using a chat interface.
   - Utilizes embeddings to find relevant responses based on the user's question.

## Getting Started

### Prerequisites

- Docker
- Python 3.10 or higher

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/damini321/fastapi-content-processor
   cd fastapi-content-processor

2. **Set up a virtual environment:**
    python -m venv venv

3. **Activate the virtual environment:**
    - On macOS/Linux: 
    ``` source venv/bin/activate
    - On Windows:
    ``` venv\Scripts\activate

4. **Install the dependencies:**
    pip install -r requirements.txt

5. **Build the Docker Image:**

    docker build -t fastapi_assignment .

6. **Run the Docker Container:**

    docker run -d -p 8000:8000 fastapi_assignment

### API Endpoints
    1. Process Web URL API

        Endpoint: POST /process_url
        Request Body (JSON): 
        {
            "url": "https://example.com"
        }
        Response:
        {
            "chat_id": "unique_chat_id",
            "message": "URL content processed and stored successfully."
        }

    2. Process PDF Document API

        Endpoint: POST /process_pdf
        Request Body: Multipart/form-data with the PDF file uploaded
        Response:
        {
            "chat_id": "unique_chat_id",
            "message": "PDF content processed and stored successfully."
        }

    3. Chat API

        Endpoint: POST /chat
        Request Body (JSON):
        {
            "chat_id": "unique_chat_id",
            "question": "What is the main idea of the document?"
        }
        Response:
        {
            "response": "The main idea of the document is..."
        }

## Dependencies
    - FastAPI
    - Uvicorn
    - BeautifulSoup4
    - pdfplumber
    - Sentence-Transformers
    - Requests
    - Python-Multipart

## Testing
#### To test the APIs:
- Use tools like Postman or curl to make requests to the running service.
- Ensure all endpoints are working as expected.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
