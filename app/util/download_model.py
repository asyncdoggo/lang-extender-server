# write a helper function to download a model from given huggingface model name and save it to the given path.

def download_model(model_name: str, path: str):
    from transformers import pipeline

    completion = pipeline("text-generation", model=model_name)
    completion.save_pretrained(path)