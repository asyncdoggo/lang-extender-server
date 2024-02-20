from fastapi import APIRouter
from argostranslate.translate import translate
from pydantic import BaseModel
import json
import bs4
from app.util.language import get_similar_words


router = APIRouter()


class TranslationRequest(BaseModel):
    from_code: str
    to_code: str
    text: str

class TranslationResponse(BaseModel):
    translation: str
    from_code: str
    to_code: str

@router.post("/translate/")
def translate_text(request: TranslationRequest):

    if request.text.strip() == "":
        return TranslationResponse(translation="", from_code=request.from_code, to_code=request.to_code)

    # If there is only one word, add meaning to it
    if len(request.text.strip().split()) == 1:
        meaning, similar_words = get_similar_words(request.text, request.from_code)
        translation = translation=translate(request.text, request.from_code, request.to_code)
        return_text = f"{translation}\n\n Meaning: {meaning}\n\n Similar words: {', '.join(similar_words)}"
        return TranslationResponse(translation=return_text, from_code=request.from_code, to_code=request.to_code)
    
    translation = translate(request.text, request.from_code, request.to_code)
    return TranslationResponse(translation=translation, from_code=request.from_code, to_code=request.to_code)

@router.get("/translate/list/")
def available_languages():
    with open('installed_packages.json', 'r') as f:
        data = json.load(f)
    return data


@router.post("/translate/page/")
def translate_page(request: TranslationRequest):
    # extract all text from text(HTML) and translate it
    print(f"Translating from {request.from_code} to {request.to_code}")
    # soup = bs4.BeautifulSoup(request.text, 'html.parser')
    # for tag in soup.find_all(True):
    #     if tag.string:
    #         tag.string = translate(tag.string, request.from_code, request.to_code)
    # return str(soup)

    return request.text
