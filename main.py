from email.mime import application
from logging import shutdown
import speech_recognition as sr
import pyjokes
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
import ctypes
import time
import win32com.client as wincl
import datetime
import pywhatkit
import subprocess

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


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
        elif 'send a mail' in query:
            try:
                talk("What should I say?")
                content = take_input()
                talk("whome should i send")
                to = input()   
                sendEmail(to, content)
                talk("Email has been sent !")
            except Exception as e:
                print(e)
                talk('I am not able to send this mail.')
       
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        
        elif 'open' in query:
            query = query.replace('open','')
            talk('Opening'+ query)
            os.system(query)
        
        elif 'shutdown' in query:
            talk('Hold on! Shutting down the device')
            subprocess.call('shutdown / p /f')

        elif "don't listen" or 'stop listening' in query:
            talk('okay, but for how much time do you want me to shut up?')
            a = int(take_input())
            time.sleep(a)
            print(a) 

        elif 'restart the device' in query:
            talk('Restarting the system')
            subprocess.call(['shutdown','/r'])        
            
        elif 'turn off' or 'exit' in query:
            talk('Turning off')
            exit()
        

        




