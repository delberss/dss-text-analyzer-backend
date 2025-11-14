from fastapi import FastAPI

app = FastAPI(title="Text Analyzer API")

from pydantic import BaseModel
from typing import List, Dict, Any

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    letters: int
    letters_no_space: int
    words: int
    sentences: int
    lines: int
    avg_words_per_sentence: float
    density: float
    top_words: List[Dict[str, Any]]


@app.get("/first")
def health():
    return {"status": "Funcionando"}
