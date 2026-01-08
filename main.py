from fastapi import FastAPI
from google.cloud import firestore

app = FastAPI()

db = firestore.Client()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profile")
def get_profile():
    docs = db.collection("profile").stream()
    return [doc.to_dict() for doc in docs]
