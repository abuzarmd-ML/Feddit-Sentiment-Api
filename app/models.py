# app/models.py
from pydantic import BaseModel

class CommentSentiment(BaseModel):
    id: str
    text: str
    polarity_score: float
    classification: str