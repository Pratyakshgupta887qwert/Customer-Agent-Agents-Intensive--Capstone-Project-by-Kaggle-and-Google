from fastapi import FastAPI
from pydantic import BaseModel
from app import Coordinator

app = FastAPI(title="Customer Intent Agent")
agent = Coordinator()

class MessageIn(BaseModel):
    text: str

class ResponseModel(BaseModel):
    intent: str
    urgency: str
    reply: str

@app.post("/predict", response_model=ResponseModel)
def predict(msg: MessageIn):
    return agent.ask(msg.text)

@app.get("/health")
def health():
    return {"status": "ok"}
