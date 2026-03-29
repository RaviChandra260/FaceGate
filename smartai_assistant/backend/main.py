from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, HTTPException
import face_recognition
import pickle
import numpy as np
import os
from contextlib import asynccontextmanager

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "faces.pkl")

# Global variable to hold the face database
face_db = {}

# Load the DB once on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    global face_db
    if os.path.exists(MODEL_PATH):
        print(f"Loading model from {MODEL_PATH}...")
        with open(MODEL_PATH, "rb") as f:
            face_db = pickle.load(f)
    else:
        print("Warning: faces.pkl not found. Database is empty.")
    yield
    # Clean up resources if needed
    face_db.clear()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "SmartAI backend running"}

# REMOVED "async" here to prevent blocking the event loop
@app.post("/face/verify")
def verify_face(file: UploadFile = File(...)):
    # usage of global face_db variable
    if not face_db:
        return {"success": False, "reason": "No registered users"}

    # Load image from the uploaded file
    image = face_recognition.load_image_file(file.file)
    encs = face_recognition.face_encodings(image)

    if not encs:
        return {"success": False, "reason": "No face detected"}

    # Verify against the loaded DB
    unknown = encs[0]
    names = list(face_db.keys())
    known_encs = list(face_db.values())

    distances = face_recognition.face_distance(known_encs, unknown)
    min_dist = np.min(distances)

    # Threshold Note: 0.45 is very strict (high security). 
    # Standard is usually 0.6. If it fails too often, try 0.5 or 0.55.
    if min_dist < 0.45:
        name = names[np.argmin(distances)]
        return {"success": True, "user": name, "confidence": float(1 - min_dist)}

    return {"success": False, "reason": "Unknown face", "distance": float(min_dist)}
#uvicorn main:app --reload