from typing import List, Optional
from fastapi import APIRouter
from lexilang.detector import detect
from pydantic import BaseModel

from app.util.language import get_similar_words

router = APIRouter()


class DetectionRequest(BaseModel):
    text: str
    languages: Optional[List[str]] = []


class DetectionResponse(BaseModel):
    language: str
    confidence: float

class WordDetailsResponse(BaseModel):
    meaning: List[str]
    similar_words: List[str]


@router.post("/detect/")
def detect_language(request: DetectionRequest):
    language, confidence = detect(request.text, request.languages)
    return DetectionResponse(language=language, confidence=confidence)


@router.get("/word/similar/")
def word_details(word: str, language_code: str, max_results: int = 5):
    meaning, similar_words = get_similar_words(word, language_code, max_results)
    return WordDetailsResponse(meaning=meaning, similar_words=similar_words)
    