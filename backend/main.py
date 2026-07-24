from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import URLRequest
from backend.parser import analyze_url

app = FastAPI(
    title="Page Pulse API",
    version="1.0.0",
    description="Website auditing API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Page Pulse API Running"
    }


@app.post("/audit")
def audit(request: URLRequest):
    return analyze_url(request.url)