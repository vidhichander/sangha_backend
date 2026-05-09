from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# CHANGE this filename to your exported .py filename
from conversation_model import on_recommendation_button_click

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    conversation_text: str
    avg_response_times_minutes: float
    message_count_a: int
    message_count_b: int
    conversation_days: float
    avg_message_length: float
    last_response_hours_ago: float
    sender_user_id: str
    receiver_user_id: str

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = on_recommendation_button_click(
        conversation_text=request.conversation_text,
        avg_response_times_minutes=request.avg_response_times_minutes,
        message_count_a=request.message_count_a,
        message_count_b=request.message_count_b,
        conversation_days=request.conversation_days,
        avg_message_length=request.avg_message_length,
        last_response_hours_ago=request.last_response_hours_ago,
        sender_user_id=request.sender_user_id,
        receiver_user_id=request.receiver_user_id,
    )

    return result