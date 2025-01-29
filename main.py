from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.faq import FAQ  # Assuming your FAQ class is in src/faq.py

# Initialize FastAPI app
app = FastAPI()

# Initialize FAQ system
faq_system = FAQ()

# Pydantic model for request body
class UserQuery(BaseModel):
    user_id: str
    question: str

# Endpoint to handle user queries
@app.post("/ask")
async def ask_question(query: UserQuery):
    user_id = query.user_id.strip()
    question = query.question.strip()

    if not user_id:
        raise HTTPException(status_code=400, detail="User ID is required.")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required.")

    # Get response from FAQ system
    response = faq_system.chat_function(question, user_id=user_id)

    return {"response": response}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce FAQ API!"}