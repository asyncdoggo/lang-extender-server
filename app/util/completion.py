from transformers import pipeline


class Completion:
    def __init__(self):
        self.completion = pipeline("text-generation", model="models/gpt2")

    def generate(self, prompt):
        return self.completion(prompt, max_new_tokens=3)[0]["generated_text"]