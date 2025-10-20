from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.database import get_current_user, get_db
from models.models import ChatMessage, User
from pydantic import BaseModel

chat_router = APIRouter(prefix="/chat", tags=["Chat"])

# -------------------- Pydantic Schemas --------------------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    message: str
    response: str

class ChatHistoryResponse(BaseModel):
    id: int
    message: str
    response: str
    created_at: str

# -------------------- Routes --------------------

# Send a message and get chatbot response
@chat_router.post("/", response_model=ChatResponse)
def send_message(
    chat: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # Here you can call your chatbot backend or AI model
    user_msg = chat.message
    bot_response = f"Echo: {user_msg}"  # replace with actual AI call

    # Save to DB
    chat_record = ChatMessage(
        user_id=current_user.id,
        message=user_msg,
        response=bot_response
    )
    db.add(chat_record)
    db.commit()
    db.refresh(chat_record)

    return {"message": user_msg, "response": bot_response}

# Get chat history of current user
@chat_router.get("/history", response_model=List[ChatHistoryResponse])
def get_chat_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    history = db.query(ChatMessage).filter(ChatMessage.user_id == current_user.id).order_by(ChatMessage.created_at.desc()).all()
    return history
