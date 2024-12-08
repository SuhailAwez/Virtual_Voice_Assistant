import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import logging
import sys

# Initialize Logging
logging.basicConfig(
    filename='assistant.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)


def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    assname = "Atlas"
    speak("I am your Assistant")
    speak(assname)


def username():
    """Greet the user and ask for their name."""
    speak("What should I call you sir?")
    uname = takeCommand()

    if uname.lower() != "none":
        speak(f"Welcome Mister {uname}")
        columns = shutil.get_terminal_size().columns

        print("#####################".center(columns))
        print(f"Welcome Mr. {uname}".center(columns))
        print("#####################".center(columns))

        speak("How can I help you, Sir?")
    else:
        speak("I didn't catch that. Please restart and tell me your name.")
        sys.exit()


def takeCommand():
    """Listen for user input and convert it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        logging.info("Listening for user input.")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        logging.info("Recognizing user input.")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        logging.info(f"User said: {query}")
    except Exception as e:
        logging.error(f"Error recognizing voice: {e}")
        print("Unable to Recognize your voice.")
        speak("Sorry, I didn't catch that. Please try again.")
        return "None"

    return query


def sendEmail(to, content):
    """Send an email using SMTP."""
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')

    if not EMAIL_USER or not EMAIL_PASS:
        speak("Email credentials are not set. Please configure environment variables.")
        return

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to, content)
        server.close()
        speak("Email has been sent successfully.")
        logging.info(f"Email sent to {to}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        speak("Sorry, I was unable to send the email.")


def main():
    """Main function to run the assistant."""
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                logging.error(f"Wikipedia error: {e}")
                speak("Sorry, I couldn't find that information on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\YourUser\\Music'  # Update to your music directory
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music")
                else:
                    speak("No music files found.")
            except Exception as e:
                logging.error(f"Music play error: {e}")
                speak("I couldn't play music due to an error.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'send email' in query or 'email to' in query:
            try:
                speak("Who is the recipient?")
                recipient = takeCommand()
                to = 'recipient@example.com'  # Replace with actual recipient email
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
            except Exception as e:
                logging.error(f"Send email error: {e}")
                speak("Sorry, I am not able to send this email.")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'exit' in query or 'quit' in query or 'shutdown' in query:
            speak("Goodbye Sir!")
            sys.exit()

        # Add more commands as needed


if __name__ == "__main__":
    main()
