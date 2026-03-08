from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="Personality-Aware Chat AI")

app.include_router(chat_router, prefix="/chat", tags=["chat"])


@app.get("/")
def root():
    return {"message": "Server is running"}