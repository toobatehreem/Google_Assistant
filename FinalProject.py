import speech_recognition as sp
import speak as s
from WeatherForecast import temp
from SendingEmail import send_mail
from MakingaDictionary import dictionary
import webbrowser as wb
from Greeting import wishes, wishMe

gap = "\t\t\t\t\t\t\t\t\t\t\t\t"


def commands():
    r1 = sp.Recognizer()
    r2 = sp.Recognizer()
    r3 = sp.Recognizer()
    r4 = sp.Recognizer()
    r5 = sp.Recognizer()
    r6 = sp.Recognizer()
    r7 = sp.Recognizer()
    r8 = sp.Recognizer()

    with sp.Microphone() as source:
        print('Try the Following commands')
        print('For YouTube you can say "Watch a Video"')
        print('For Browser you can say "Browse on Google"')
        print('For Sending an E-mail you can say "Send an E-mail"')
        print('For Searching the meaning of a word you can say "Dictionary"')
        print('For Weather you can say "Weather"')
        print('To quit you can say "Bye"')
        print("Speak Now")
        audio = r1.listen(source)

    if 'video' in r2.recognize_google(audio):
        print(gap + "Video")
        r2 = sp.Recognizer()
        url = 'www.youtube.com/results?search_query='
        with sp.Microphone() as source:
            print('Search for a Video on YouTube\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(gap + get)
                print("Searching " + get + " on YouTube")
                s.my_speak("Searching " + get + " on YouTube")
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                wb.get(chrome_path).open(url + get)
                commands()
            except sp.UnknownValueError:
                print('Error')
                commands()
            except sp.RequestError as e:
                print("Failed".format(e))

    elif 'browse' in r3.recognize_google(audio):
        print(gap + "Browse on Google")
        r3 = sp.Recognizer()
        url = 'www.google.com/search?q='
        with sp.Microphone() as source:
            print("Search for a query on Google\n")
            audio = r3.listen(source)

            try:
                get = r3.recognize_google(audio)
                print(gap + get)
                print("Searching " + get + " on Google")
                s.my_speak("Searching " + get + " on Google")
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                wb.get(chrome_path).open(url+get)
                commands()
            except sp.UnknownValueError:
                print('Error')
                commands()
            except sp.RequestError as e:
                print('Failed'.format(e))

    elif 'email' in r4.recognize_google(audio):
        print(gap + 'Send an E-mail')
        r4 = sp.Recognizer()
        s.my_speak("Kindly use keyboard to Enter the Receiver's Email Address: ")
        RECEIVER_MAIL = input("Receiver's Email Address: \t\t\t\t")
        with sp.Microphone() as source:
            print("Kindly tell me the subject")
            s.my_speak("Kindly tell me the subject")
            subject = r4.listen(source)

            try:
                get = r4.recognize_google(subject)
                print(gap + get)
            except sp.UnknownValueError:
                print('Sorry! I didn''t understand your subject')
                commands()
            except sp.RequestError as e:
                print("Failed to understand the subject".format(e))
                s.my_speak("Failed to understand the subject")
                commands()
        with sp.Microphone() as source:
            print('Kindly tell me the message')
            s.my_speak('Kindly tell me the message')
            msg = r4.listen(source)

            try:
                get1 = r4.recognize_google(msg)
                print(gap + get1)
                send_mail(get, get1, RECEIVER_MAIL)
                commands()
            except sp.UnknownValueError:
                print('Sorry! I didn''t understand your message')
                s.my_speak("Failed to understand the message")
                commands()
            except sp.RequestError as e:
                print("Failed to understand the message".format(e))
                commands()

    elif 'dictionary' in r5.recognize_google(audio):
        print(gap + "Dictionary")
        r5 = sp.Recognizer()
        dictionary()
        commands()

    elif 'weather' in r6.recognize_google(audio):
        print(gap + "Weather")
        r6 = sp.Recognizer()
        with sp.Microphone() as source:
            print("Kindly tell the City name: ")
            s.my_speak("Kindly tell the City name: ")
            name = r6.listen(source)

            try:
                get = r6.recognize_google(name)
                print(gap + get)
                temp(get)
                commands()
            except sp.UnknownValueError:
                print('Error')
                commands()
            except sp.RequestError as e:
                print("Failed".format(e))
    elif 'bye' in r7.recognize_google(audio):
        print(gap + "Bye")
        print("It was nice talking to you. Good Bye...")
        s.my_speak("It was nice talking to you Good Bye...")
        exit()

    else:
        r8 = sp.Recognizer()
        with sp.Microphone() as source:
            url = 'www.google.com/search?q='
            new_command = r8.listen(source)

            try:
                get = r8.recognize_google(new_command)
                print(gap + get)
                print('Searching...')
                s.my_speak('Searching')
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                wb.get(chrome_path).open(url + get)
                commands()
            except sp.UnknownValueError:
                print('Error')
                commands()
            except sp.RequestError as e:
                print('Failed '.format(e))


if __name__ == '__main__':
    wishes()
    wishMe()
    commands()
