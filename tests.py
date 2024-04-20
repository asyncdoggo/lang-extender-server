from app.app import app

from fastapi.testclient import TestClient

import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_main(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        

    def test_detect_language(self):
        response = self.client.post("/detect/", json={"text": "hello"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["language"], "en")

    def test_similar_word(self):
        response = self.client.get("/word/similar/?word=hello&language_code=en")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn("meaning", data)
        self.assertIn("similar_words", data)

    def test_translate_text(self):
        response = self.client.post("/translate/", json={"from_code": "en", "to_code": "fr", "text": "hello"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["translation"], "Bonjour.")

    def test_available_languages(self):
        response = self.client.get("/translate/list/")
        self.assertEqual(response.status_code, 200)


    def test_complete_text(self):
        response = self.client.post("/completion/", json={"text": "hello"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("completion", data)
        print(data["completion"])


if __name__ == "__main__":
    unittest.main()