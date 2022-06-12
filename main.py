import time

import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said:{query}\n")

    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you're welcome, sir")
                elif "thanks" in query:
                    speak("you're welcome, sir")
                elif "open" in query:
                    from DictApp import openwebapp
                    openwebapp(query)
                elif "close" in query:
                    from DictApp import closewebapp
                    closewebapp(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import  searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in HAVEYLIYAA"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in HAVEYLIYAA"        #this is the city of which we are checking weather
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    weather = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {weather}")

                elif ("set an alarm") in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done, Sir")

                elif "the time" in query:
                    time1 = time.localtime()
                    current_time = time.strftime("%H: %M", time1)
                    current_time1 = int (time.strftime("%H", time1))
                    current_time2 = time.strftime("%M", time1)

                    if current_time1>=0 and current_time1<12:
                        speak("The time is"+current_time+"AM")
                    else:
                        current_time = (current_time1) - (12)
                        speak(f"The time is {current_time} {current_time2} PM")

                elif "sleep finally" in query:
                    speak("Going to sleep, sir")
                    exit()










