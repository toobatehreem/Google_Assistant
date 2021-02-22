import speech_recognition as sp
import speak as s
import datetime

gap = "\t\t\t\t\t\t\t\t\t\t\t\t"


def wishes():
    r1 = sp.Recognizer()
    r2 = sp.Recognizer()
    with sp.Microphone() as source:
        print("Use trigger word 'Hello'")
        audio = r1.listen(source)

    if 'hello' in r2.recognize_google(audio):
        print(gap + "Hello")
        r2 = sp.Recognizer()
        with sp.Microphone() as source:
            print('Hello. This is your assistant Hazel. \nMay I know your good name?')
            s.my_speak('Hello. This is your assistant Hazel. May I know your good name')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(gap + get)
                print('Hi ' + get)
                s.my_speak('Hi' + get)
            except sp.UnknownValueError:
                print('Error')
            except sp.RequestError as e:
                print("Failed".format(e))

def wishMe():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    if hour >= 0 and hour < 12:
        s.my_speak('Good Morning')
        s.my_speak('It is ' + str(hour) + ':' + str(min) + ' AM')
        print('How may I help you?')
        s.my_speak('How may I help you?')

    elif hour >= 12 and hour < 18:
        s.my_speak('Good Afternoon')
        s.my_speak('It is ' + str(hour) + ':' + str(min) + ' PM')
        print('How may I help you?')
        s.my_speak('How may I help you?')

    else:
        s.my_speak('Good Evening')
        s.my_speak('It is ' + str(hour) + ':' + str(min) + ' PM')
        print('How may I help you?')
        s.my_speak('How may I help you?')
