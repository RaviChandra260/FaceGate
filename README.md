# 🤖 FaceGate — Smart AI Assistant

A final year AI project that combines **Face Recognition Access Control**, **Voice Assistant**, and **Speech Translation** into one unified system — built with Python, FastAPI, and Streamlit.

---

## ✨ Features

- 🔐 **Face Recognition Login** — Camera detects and authenticates users in real-time
- ✅ **Access Granted / Denied** — Voice announces result instantly
- 📸 **Face Registration** — Register new users with a single photo
- 🎙️ **Voice Assistant** — Hands-free voice command control
- 🌍 **Speech Translator** — Multilingual voice translation
- ⚡ **FastAPI Backend** — REST API for face verification
- 🖥️ **Streamlit Frontend** — Clean web UI for all features
- 🔑 **JWT Authentication** — Secure token-based auth system

---

## 🗂️ Project Structure

```
FaceGate/
│
├── smartai_assistant/
│   ├── backend/
│   │   ├── main.py              # FastAPI server & /face/verify endpoint
│   │   ├── auth/
│   │   │   └── jwt_handler.py   # JWT token creation & validation
│   │   ├── face_auth/
│   │   │   ├── register.py      # Register a new face into the model
│   │   │   └── verify.py        # Real-time webcam face verification
│   │   └── voice/
│   │       ├── test_tts.py      # Text-to-speech test
│   │       └── test_voice.py    # Speech recognition test
│   │
│   └── frontend/
│       └── app.py               # Streamlit web UI
│
├── data/                        # Face images (gitignored)
├── models/                      # Trained face model faces.pkl (gitignored)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Face Recognition | face_recognition, OpenCV |
| Voice | pyttsx3, SpeechRecognition |
| Auth | JWT (python-jose) |
| ML Model | pickle (.pkl) |

---

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/RaviChandra260/FaceGate.git
cd FaceGate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Register your face**
```bash
# Place your photo as data/YourName.jpg first, then:
python smartai_assistant/backend/face_auth/register.py
```

**4. Start the FastAPI backend**
```bash
cd smartai_assistant/backend
uvicorn main:app --reload
```

**5. Start the Streamlit frontend**
```bash
cd smartai_assistant/frontend
streamlit run app.py
```

---

## 📋 Requirements

```
fastapi
uvicorn
streamlit
face_recognition
opencv-python
numpy
pyttsx3
speechrecognition
python-jose
pyaudio
pickle5
```

---

## 🔐 How Face Authentication Works

```
User faces camera
      ↓
OpenCV captures frame
      ↓
face_recognition encodes face
      ↓
Compare with registered faces in faces.pkl
      ↓
Distance < 0.45 threshold?
      ↓
✅ GRANTED → Speak "Access Granted, [Name]"
❌ DENIED  → Show UNKNOWN
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/face/verify` | Upload image → returns match result |

**Example Response:**
```json
{
  "success": true,
  "user": "Ravi",
  "confidence": 0.87
}
```

---

## 🖥️ UI Pages

| Page | Description |
|---|---|
| Home | System overview |
| Face Registration | Register a new user |
| Face Login | Authenticate via webcam |
| Voice Assistant | Voice command control |
| Translator | Multilingual speech translation |

---

## ⚙️ Configuration

In `verify.py`, adjust the camera index if needed:
```python
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Change 1 → 0 for default webcam
```

Adjust recognition strictness:
```python
TOLERANCE = 0.45  # Lower = stricter. Try 0.5 or 0.55 if failing too often
```

---

## 👨‍💻 Author

**RaviChandra260**  
GitHub: [@RaviChandra260](https://github.com/RaviChandra260)

---

## 📄 License

MIT License — free to use, modify and distribute.

---

> 🎓 Final Year Project | AI-Based Smart Assistant System
