import pyttsx3
import datetime
import wikipedia
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Dom, your personal assistant, how can i help you?")


def listenCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....!!")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Understanding what you said....")
        querys = r.recognize_google(audio, language='en-in')
        print(f"You said:{querys}\n")
    except Exception as e:
        speak("I was unable to understand what you said")
        speak("Can you say that again please")
        print("Try again")
        return "None"
    return querys


if __name__ == "__main__":
    greetings()
    while True:
        querys = listenCommand().lower()

        if 'wikipedia' in querys:
            speak("Searching Wikipedia....")
            querys = querys.replace("wikipedia", "")
            results = wikipedia.summary(querys, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open chrome' in querys:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening chrome")
            os.startfile(chromePath)
        elif 'open minecraft' in querys:
            minecraftPath = "C:\\Users\\Saurabh\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            speak("Opening Minecraft")
            os.startfile(minecraftPath)
        elif 'play anime' in querys:
            anime_directory = 'D:\\Anime'
            speak("Opening Anime")
            anime = os.listdir(anime_directory)
            os.startfile(os.path.join(anime_directory, anime[0]))
        elif 'play music' in querys:
            speak("Opening Spotify")
            spotifyPath = "C:\\Users\\Saurabh\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)
        elif 'Google' in querys:
            speak("Opening Google")
            chromePath2 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath2)
        elif 'time' in querys:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strtime}")
