import os
import pyttsx3
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr

engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voice', voices[1].id)

def speekaudio(command):

    engin.say(command)
    engin.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speekaudio("Good Morning")
    elif hour >= 12 and hour < 18:
        speekaudio("Good Afternoon")
    else:
        speekaudio("Good Evening")
    speekaudio("Alexa here how may i help you")


def goto(query):
    if query == "open google":
        webbrowser.open_new('google.com')
    elif query == "open youtube":
        webbrowser.open_new('youtube.com')

    elif "Wikipedia" in query:
         speekaudio('searching wikipeddia..')
         query = query.replace('wikipedia' , "")
         results = wikipedia.summary(query ,sentences = 2)
         speekaudio("acoording to wikipedia")
         speekaudio(results)
    elif " slack" in query:
        path = "C:\\Users\\mt\\AppData\\Local\\slack\\slack.exe"
        os.startfile(path)
    else:
        speekaudio("Sorry say that again")
        query = takecommand().lower()
        goto(query)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recogniziing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"you said: {query}\n")
        speekaudio(query)

    except Exception as e:
        print(e)

        print("Say That Again ")
        return "none"
    return query


if __name__ == '__main__':
    wishme()
    query = takecommand().lower()
