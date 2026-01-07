import webbrowser
import openai
import speech_recognition as sr
import os
import datetime
def say(text):
    os.system(f"say {text}" )


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =1
        audio = r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"You said: {query}")
            return query
        except Exception as e:
            return "Some error occurred"
if __name__ == '__main__':
    print("Welcome to Speech Recognition")
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query= takecommand()
        sites=[["Youtube","https://www.youtube.com"],["Google","https://www.google.com"],["Wikipedia","https://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0] }".lower() in query.lower():
                say(f"Opening {site[0]} sir..")
                webbrowser.open_new_tab(site[1])

        if"open music" in query:
            musicPath="/Users/mayanksinghal/Downloads/WhatsApp\ Audio\ 2026-01-07\ at\ 18.45.03.mpeg"
            import subprocess, sys
            opener="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener,musicPath])
        if "the time" in query:
            musicPath = "/Users/mayanksinghal/Downloads/WhatsApp\ Audio\ 2026-01-07\ at\ 18.45.03.mpeg"
            import subprocess, sys
            strfTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            say(f"Sir the time is {strfTime}")
        if"open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
        #say(query)


