import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidade da fala
    engine.setProperty('volume', 1)  # Volume (0.0 a 1.0)
    engine.say(text)
    engine.runAndWait()
