import face_recognition
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_PATH = os.path.join(BASE_DIR, "models", "faces.pkl")

name = input("Enter your name: ").strip()
img_path = os.path.join(DATA_DIR, f"{name}.jpg")

if not os.path.exists(img_path):
    raise FileNotFoundError(f"Image not found: {img_path}")

img = face_recognition.load_image_file(img_path)
encodings = face_recognition.face_encodings(img)

if len(encodings) != 1:
    raise RuntimeError("Image must contain exactly ONE face")

encoding = encodings[0]

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        data = pickle.load(f)
else:
    data = {}

data[name] = encoding

with open(MODEL_PATH, "wb") as f:
    pickle.dump(data, f)

print(f"Face registered successfully for {name}")
