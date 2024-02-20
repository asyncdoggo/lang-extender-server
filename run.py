from app.app import app

from fastapi.testclient import TestClient

if __name__ == "__main__":
    # client = TestClient(app)

    # response = client.post("/detect/", json={"text": "Bonjour, comment ça va?"})

    # print(response.json())

    # response = client.get("/translate/list/")

    # print(response.json())

    # response = client.post("/translate/", json={"from_code": "fr", "to_code": "en", "text": "Bonjour, comment ça va?"})

    # print(response.json())

    # response = client.get("/word/similar/?word=bonjour&language_code=fr&max_results=5")

    # print(response.json())

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)