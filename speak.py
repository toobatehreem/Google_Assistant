import pyttsx3
import datetime

def my_speak(message):
    engine = pyttsx3.init('sapi5')
    '''voices = engine.getProperty('voices')
    print(voices[0].id)
    engine.setProperty('voice', voices[0].id)'''
    engine.say('{}' .format(message))
    engine.runAndWait()
