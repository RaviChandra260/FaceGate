import cv2
import face_recognition
import pickle
import os
import numpy as np
import pyttsx3
import threading  # Added for non-blocking audio

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "faces.pkl")

# (Keep your existing path checks here...)
if not os.path.exists(MODEL_PATH):
    # For testing, creating dummy data if file missing (Remove this in prod)
    print("Warning: Model file not found.")
    known_faces = {} 
else:
    with open(MODEL_PATH, "rb") as f:
        known_faces = pickle.load(f)

known_names = list(known_faces.keys())
known_encodings = list(known_faces.values())

# ---------------- VOICE FUNCTION ----------------
def speak(text):
    """Runs text-to-speech in a separate thread to prevent video freezing"""
    def _speak():
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        engine.say(text)
        engine.runAndWait()
    
    thread = threading.Thread(target=_speak)
    thread.start()

spoken = set()

# ---------------- CAMERA ----------------
# FIX: Changed from 1 to 0 (Standard Webcam)
# If 0 is DroidCam, change this to 2, or disable DroidCam in Device Manager.
# CAP_DSHOW forces Windows to look for hardware cameras first
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) 

print("Face verification started. Press Q to quit.")

TOLERANCE = 0.45 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read from webcam. Check if blocked by another app.")
        break

    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, locations)

    for (top, right, bottom, left), enc in zip(locations, encodings):
        distances = face_recognition.face_distance(known_encodings, enc)
        
        name = "UNKNOWN"
        color = (0, 0, 255)

        # Check if we have any known faces to compare against
        if len(distances) > 0:
            min_dist = np.min(distances)
            if min_dist < TOLERANCE:
                idx = np.argmin(distances)
                name = known_names[idx]
                color = (0, 255, 0)

                if name not in spoken:
                    # FIX: Using the threaded speak function
                    speak(f"Access granted {name}")
                    spoken.add(name)

        # Scale coords back up
        top, right, bottom, left = [v * 4 for v in (top, right, bottom, left)]

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Face Authentication", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()