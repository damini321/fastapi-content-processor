# app/services.py
import requests
from bs4 import BeautifulSoup
import pdfplumber
from sentence_transformers import SentenceTransformer, util

# 1. Scraping the web URL
def process_url_content(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join(soup.stripped_strings)
    return text

# 2. Processing the PDF file
async def process_pdf_content(file) -> str:
    with pdfplumber.open(file.file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return ' '.join(text.split())

# 3. Embedding-based search (Using SentenceTransformers)
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(content: str):
    sentences = content.split('.')
    embeddings = model.encode(sentences, convert_to_tensor=True)
    return sentences, embeddings

def search_query(content: str, question: str) -> str:
    sentences, embeddings = generate_embeddings(content)
    query_embedding = model.encode(question, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    best_sentence = sentences[cosine_scores.argmax()]
    return best_sentence
