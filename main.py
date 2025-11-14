from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi import HTTPException

import re
from collections import Counter

app = FastAPI(title="Text Analyzer API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

_WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)
_SENTENCE_RE = re.compile(r"[.!?]+")

def analyze_text(text: str) -> dict:
    if text is None:
        text = ""

    letters = len(text)
    letters_no_space = len(re.sub(r"\s+", "", text))

    words_list = _WORD_RE.findall(text.lower())
    words = len(words_list)

    sentences = len(_SENTENCE_RE.findall(text))
    if sentences == 0 and words > 0:
        sentences = 1

    lines = 1 if text == "" else len(re.split(r"\r\n|\r|\n", text))

    avg_words_per_sentence = round((words / sentences) if sentences else 0, 2)
    density = round((letters_no_space / words) if words else 0, 2)

    counter = Counter(words_list)
    top = [{"word": w, "count": c} for w, c in counter.most_common(10)]

    return {
        "letters": letters,
        "letters_no_space": letters_no_space,
        "words": words,
        "sentences": sentences,
        "lines": lines,
        "avg_words_per_sentence": avg_words_per_sentence,
        "density": density,
        "top_words": top,
    }

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    text = req.text

    if not isinstance(text, str):
        raise HTTPException(status_code=400, detail="text must be a string")

    result = analyze_text(text)
    return result

@app.get("/health")
def health():
    return {"status": "ok"}
