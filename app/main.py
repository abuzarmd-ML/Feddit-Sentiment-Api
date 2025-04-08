# app/main.py
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Feddit Sentiment Analyzer")

app.include_router(router)
