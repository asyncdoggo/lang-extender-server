import argostranslate
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from app.routers import translate, detect, completion
import app.setup as setup
from app.util.download_model import download_model


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(translate.router)
app.include_router(detect.router)
app.include_router(completion.router)

def setup_packages():
    available_packages = argostranslate.package.get_available_packages()

    pack_list = []

    for i in available_packages:
        if i.from_code == "en" and i.to_code == "fr":
            pack_list.append(i)

        if i.from_code == "fr" and i.to_code == "en":
            pack_list.append(i)

    setup.install_packages(pack_list, False)

setup_packages()



download_model("gpt2", "models/gpt2")


@app.get("/")
def read_root():
    # redirect to docs
    return RedirectResponse(url="/docs")
