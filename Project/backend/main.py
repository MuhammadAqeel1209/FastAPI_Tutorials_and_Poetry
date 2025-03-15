from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  # type: ignore # PyMuPDF for PDF parsing
import spacy
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this if using a different frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure spaCy model is available
MODEL_NAME = "en_core_web_sm"
if not spacy.util.is_package(MODEL_NAME):
    os.system(f"python -m spacy download {MODEL_NAME}")

nlp = spacy.load(MODEL_NAME)  # Load spaCy model

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    # Ensure file is a PDF
    if not file.filename.endswith(".pdf"): # type: ignore
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    content = await file.read()

    try:
        text = extract_text_from_pdf(content)
        analysis = analyze_text(text)
        return {"filename": file.filename, "analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def extract_text_from_pdf(pdf_bytes):
    """Extracts text from a given PDF file bytes."""
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "\n".join(page.get_text("text") for page in doc)
        return text.strip()
    except Exception as e:
        raise ValueError(f"Error processing PDF: {str(e)}")

def analyze_text(text):
    """Analyzes text using spaCy NLP model."""
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return {"word_count": len(text.split()), "keywords": keywords[:10]}
