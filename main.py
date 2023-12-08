import datetime
import json
import os
import webbrowser as wb
import pyautogui
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia
import subprocess
import ctypes
from ctypes import wintypes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the time is")
    speak(Time)
    print("The time is ", Time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the todays date is")
    speak(day)
    speak(month)
    speak(year)
    print("The todays date is " + str(day) + "/" + str(month) + "/" + str(year))


def wishme():
    print("Welcome back Rugwed!!")
    speak("Welcome back Rugwed!!")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning !!")
        print("Good Morning !!")
    elif 12 <= hour < 16:
        speak("Good Afternoon !!")
        print("Good Afternoon !!")
    elif 16 <= hour < 24:
        speak("Good Evening !!")
        print("Good Evening !!")
    else:
        speak("Good Night")
        print("Good Night")


def greetme():
    print("Bye Bye Rugwed, See you again.")
    speak("Bye Bye Rugwed, See you again.")


def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\\CODES\\PyCharm Projects\\Desktop_Assistant\\screenshots\\ss3.png")


def lock_screen():
    ctypes.windll.user32.LockWorkStation()


def sleep_system():
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 10
        try:
            audio = r.listen(source, timeout=20, phrase_time_limit=20)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please say it again.")
            speak("Sorry, I didn't catch that. Please say it again.")
            return "Try Again"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("I'm having trouble connecting to the speech recognition service.")
            return "Try Again"


if __name__ == "__main__":
    wishme()
    trigger_phrase = "hello assistant"
    while True:
        query = takecommand().lower()
        if trigger_phrase in query:
            speak("How can I assist you?")
            while True:
                query = takecommand().lower()
                if "time" in query:
                    time()
                elif "date" in query:
                    date()
                elif "who are you" in query:
                    speak("I'm a desktop voice assistant.")
                    print("I'm a desktop voice assistant.")
                elif "how are you" in query:
                    speak("I'm fine, What about you?")
                    print("I'm fine, What about you?")
                elif "fine" in query or "good" in query:
                    speak("Glad to hear that !!")
                    print("Glad to hear that !!")
                elif "wikipedia" in query:
                    try:
                        speak("Ok wait, I'm searching...")
                        query = query.replace("wikipedia", "")
                        result = wikipedia.summary(query, sentences=2)
                        print(result)
                        speak(result)
                    except Exception as e:
                        speak("Can't find this page, please ask something else")
                elif "search" in query and "website" in query:
                    website_name = query.replace("search", "").replace("website", "").strip()
                    speak(f"Opening {website_name} on Google Chrome.")
                    subprocess.Popen(['start', 'chrome', f'https://{website_name}'], shell=True)
                    break
                elif "lock screen" in query:
                    lock_screen()
                    speak("Screen locked.")
                elif "sleep" in query or "put to sleep" in query:
                    sleep_system()
                    speak("System going to sleep.")
                elif "play" in query:
                    try:
                        speak("Please tell me name of the song")
                        song_name = takecommand()
                        search_query = f"{song_name} song"
                        kit.playonyt(search_query)
                    except Exception as e:
                        speak(f"No results found for '{song_name}' on YouTube.")
                        print(f"No results found for '{song_name}' on YouTube.")
                elif "open microsoft edge" in query:
                    msedgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(msedgePath)
                elif "microsoft edge" in query:
                    try:
                        speak("What should I search?")
                        print("What should I search?")
                        msedgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                        search = takecommand()
                        wb.get(msedgePath).open_new_tab(search)
                        print(search)
                    except Exception as e:
                        speak("Can't open now, please try again later.")
                        print("Can't open now, please try again later.")
                elif "weather" in query:
                    try:
                        speak("What city you are in?")
                        print("What city you are in?")
                        user_api = "e383a51cd88ebd04d15807989d734a59"
                        location = takecommand()
                        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
                        api_link = requests.get(complete_api_link)
                        api_data = api_link.json()
                        temp_city = ((api_data['main']['temp']) - 273.15)
                        weather_desc = api_data['weather'][0]['description']
                        hmdt = api_data['main']['humidity']
                        wind_spd = api_data['wind']['speed']
                        date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                        speak("Weather Status for - {}  || {}".format(location.upper(), date_time))
                        print("Weather Status for - {}  || {}".format(location.upper(), date_time))
                        speak("Current temperature is: {:.2f} deg C".format(temp_city))
                        print("Current temperature is: {:.2f} deg C".format(temp_city))
                    except Exception as e:
                        speak("City can not be found, please give the valid city name.")
                        print("Can't open now, please give the valid city name.")
                elif "news" in query:
                    query_params = {
                        "source": "bbc-news",
                        "sortBy": "top",
                        "apiKey": "7427382318744029b2d9e7af7557fa9b"
                    }
                    main_url = " https://newsapi.org/v1/articles"
                    res = requests.get(main_url, params=query_params)
                    open_bbc_page = res.json()
                    articles = open_bbc_page.get("articles", [])
                    for i, article in enumerate(articles, start=1):
                        speak(f"News {i}: {article['title']}")
                        print(f"News {i}: {article['title']}")
                elif "remind me" in query:
                    speak("What should I remind you")
                    data = takecommand()
                    speak("You have told me to remind you that " + data)
                    print("You have told me to remind you that " + str(data))
                    notedown = open("reminders.txt", "w")
                    notedown.write(data)
                    notedown.close()
                elif "you have something to remind me" in query:
                    notedown = open("reminders.txt", "r")
                    speak("You told me to remind you that " + notedown.read())
                    print("You told me to remind you that " + str(notedown.read()))
                elif "notedown" in query:
                    speak("What should I notedown")
                    data = takecommand()
                    speak("You have told me to notedown " + data)
                    print("You have told me to notedown " + str(data))
                    notedown = open("notes.txt", "w")
                    notedown.write(data)
                    notedown.close()
                elif "you have any note for me" in query:
                    notedown = open("notes.txt", "r")
                    speak("You told me to notedown that " + notedown.read())
                    print("You told me to notedown that " + str(notedown.read()))
                elif "joke" in query:
                    def jokes(f):
                        data = requests.get(f)
                        tt = json.loads(data.text)
                        return tt


                    f = r"https://official-joke-api.appspot.com/jokes/programming/random"
                    a = jokes(f)

                    for i in a:
                        speak("I have a joke related to Programming")
                        print(i["type"])
                        speak(i["setup"])
                        print(i["setup"])
                        speak(i["punchline"])
                        print(i["punchline"], "\n")
                elif "screenshot" in query:
                    screenshot()
                    speak("I've taken screenshot, please check it")
                elif "shutdown" in query:
                    greetme()
                    quit()
                else:
                    speak("I'm not sure how to respond to that. Can you please repeat?")
                    print("I'm not sure how to respond to that. Can you please repeat?")
