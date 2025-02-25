from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import google.generativeai as genai #type: ignore
import os 
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

# Set Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

# Pydantic model for request body
class ContentRequest(BaseModel):
    topic: str
    content_type: str  # e.g., "blog_post", "social_media"

# Function to generate content using Gemini API
def generate_content(topic: str, content_type: str) -> str:
    prompt = f"Write a {content_type} about {topic}."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI endpoint to generate content
@app.post("/generate-content")
async def generate_content_endpoint(request: ContentRequest):
    try:
        content = generate_content(request.topic, request.content_type)
        return {"content": content}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

