import requests
import speech_recognition as sp
import pyttsx3

def my_speak(message):
    engine = pyttsx3.init()
    engine.say('{}' .format(message))
    engine.runAndWait()

def temp(city):
    api_address1 = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_address2 = '&appid=d646c8fe7ab69888e43f2d556480bbf9'

    url = api_address1 + city +api_address2

    json_data = requests.get(url).json()

    formatted_data1 = json_data['weather'][0]['main']
    formatted_data2 = json_data['main']['temp']
    Temperature = str(round(int(formatted_data2) - 273.15))

    print("It is " + Temperature + ' degrees and ' + formatted_data1 + ' in ' + city)
    my_speak("It is " + Temperature + ' degrees and ' + formatted_data1 + ' in ' + city)

r1 = sp.Recognizer()
r2 = sp.Recognizer()