import speech_recognition as sr
import pyttsx3
import pywhatkit
import datatime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.sat(text)
    engine.runAndWait()
    