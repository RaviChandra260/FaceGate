import pyttsx3

engine = pyttsx3.init(driverName='sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # force voice
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

engine.say("If you can hear this, text to speech is working.")
engine.runAndWait()
