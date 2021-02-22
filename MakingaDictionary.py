from PyDictionary import PyDictionary
import speech_recognition as sp
import speak as s
import warnings
warnings.filterwarnings("ignore")

r1 = sp.Recognizer()
r2 = sp.Recognizer()

def dictionary():
    with sp.Microphone() as source:
        print('Search for a word : ', end='')
        search_word = r1.listen(source)

        try:
            get = r2.recognize_google(search_word)
            print(get)
            myDict = PyDictionary(get)
            meaning = myDict.getMeanings()
            for values in meaning.values():
                print('Noun: ', values['Noun'][0])
                a = values['Noun'][0]
                s.my_speak(a)
        except:
            print("Not Found")
