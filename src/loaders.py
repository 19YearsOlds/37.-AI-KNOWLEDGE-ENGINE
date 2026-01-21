import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

def load_pdf(file_path: str) -> str:
    text = ""
    pdf = PdfReader(file_path)
    for page in pdf.pages:
        text += page.extract_text() + "\n"
    return text

def load_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
def load_website(url: str) -> str:
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text(separator="\n")

def load_data_from_folder(folder: str) -> dict:
    docs = {}
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".pdf"):
            docs[file] = load_pdf(path)
        elif file.endswith(".txt") or file.endswith(".md"):
            docs[file] = load_text(path)
    return docs