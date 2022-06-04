import speech_recognition as sr
import pyjokes
import pyttsx3
import wikipedia
import webbrowser
import os
import ctypes
import win32com.client as wincl
import datetime
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_input():
    try:
        with sr.Microphone() as source:
            print("Listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        talk("Good Morning !")
    
    
  
    elif hour>= 12 and hour<18:
        talk("Good Afternoon !")  
  
    else:
        talk("Good Evening !") 
  
 
    talk("What's up")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    while True:
        query = take_input().lower()
        if 'wikipedia' in query:
            talk('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 3)
            talk("According to wikipedia..")
            print(results)
            talk(results)
        elif 'open google' in query:
            talk('opening google')
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            talk('opening youtube')
            webbrowser.open("youtube.com")
        elif 'open spotify' in query:
            talk('opening spotify')
            os.system("Spotify")
        elif 'play music' or 'play a song' in query:
            talk('playing')
            pywhatkit.playonyt('50 Cent')
        elif 'joke' in query:
            talk(pyjokes.getjoke())
        elif 'lock device' in query:
            talk('Locking the screen')
            ctypes.windll.user32.LockWorkStation()


        


        elif 'turn off' in query:
            talk('Turning off')
            exit()
        


