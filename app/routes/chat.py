from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.services.llm_service import generate_text

router = APIRouter()


@router.post("/", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = generate_text(req.message)
    return ChatResponse(reply=reply)