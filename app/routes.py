# app/routes.py
from fastapi import APIRouter, Query
from app.feddit_client import get_comments
from app.sentiment import analyze_sentiment

router = APIRouter()

@router.get("/analyze/{subfeddit}")
def analyze_subfeddit(
    subfeddit: str,
    sort_by_score: bool = False,
    start_time: str = None,
    end_time: str = None
):
    comments = get_comments(subfeddit, start_time=start_time, end_time=end_time)
    analyzed = []

    for comment in comments[:25]:
        polarity, sentiment = analyze_sentiment(comment["text"])
        analyzed.append({
            "id": comment["id"],
            "text": comment["text"],
            "polarity_score": polarity,
            "classification": sentiment
        })

    if sort_by_score:
        analyzed.sort(key=lambda x: x["polarity_score"], reverse=True)

    return analyzed
