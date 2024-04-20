from fastapi import APIRouter
from argostranslate.translate import translate
from pydantic import BaseModel
import json
import bs4
from app.util.language import get_similar_words
from app.util.completion import Completion

router = APIRouter()


completion = Completion()


class CompletionRequest(BaseModel):
    text: str


@router.post("/completion/")
async def complete_text(request: CompletionRequest):
   # predict next 3 words
    completion_text = completion.generate(request.text)
    return {"completion": completion_text}
