import pyttsx3 # pip install pyttsx3 installs voice
import datetime
import requests
import speech_recognition
from urllib.request import Request, urlopen

engine = pyttsx3.init()
fps = 44100
newVoiceRate = 190
duration = 1

def speak(audio):
    engine.setProperty('rate',newVoiceRate)
    engine.say(audio)
    engine.runAndWait()

def query():
    
    recognizer = speech_recognition.Recognizer()
    print("listening...")
    text = ""
    try:
            
        with speech_recognition.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"Recognized {text}")
    except: #speech_recognition.UnkownValueError():
        recognizer = speech_recognition.Recognizer() 
         
    
    query = text
    if query.__contains__("who are you"):
        speak("i am your personal voice assistant.")
    elif query.__contains__("time") and query.__contains__("what"):
        speak(time())
    elif query.__contains__("what") or query.__contains__("how") or query.__contains__("where") or query.__contains__("why") or query.__contains__("when") or query.__contains__("who"):
        search = "https://www.google.com/search?q="+ query
        search = search.replace(" ","+")
        req = Request(url=search,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        print(webpage)

def time():
    hour = datetime.datetime.now().strftime("%I")
    timithy = ""
    if hour=="09":
        timithy=("9")
    elif hour=="08":
        timithy=("8") 
    elif hour=="07" :
        timithy=("7")
    elif hour=="06":
        timithy=("6")
    elif hour=="05":
        timithy=("5")
    elif hour=="04":
        timithy=("4")
    elif hour =="03":
        timithy=("3")
    elif hour=="02":
        timithy=("2")
    elif hour=="01":
        timithy=("1")
    else:
        timithy=(hour)  

    min = datetime.datetime.now().strftime("%M")
    bob = ""
    if min=="09":
       bob =("o9")
    elif min=="08":
        bob =("o8") 
    elif min=="07" :
        bob =("o7")
    elif min=="06":
         bob =("o6")
    elif min=="05":
       bob =("o5")
    elif min=="04":
        bob =("o4")
    elif min =="03":
        bob =("o3")
    elif min=="02":
         bob =("o2")
    elif min=="01":
       bob =("o1")
    else:
        bob=(min)  

    timithy=  timithy + " "+(bob)
    return timithy

def date():
    year = str(int(datetime.datetime.now().year))
    month = str(int(datetime.datetime.now().month))
    day = str(int(datetime.datetime.now().day))
    date = [month,day,year]
    return date

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour< 12:
        speak("Good morning sir")
        speak("the current time is "+time())
        time()
        speak("the current date is " +date()[0] + " " + date()[1] + " " + date()[2])
        date()
        speak("I am at your service. Please tell me how can I help you this morning?")
    elif hour >=12 and hour <18:
        speak("good afternoon sir.")
        speak("the current time is " +time())
        time()
        speak("the current date is " +date()[0] + " " + date()[1] + " " + date()[2])
        date()
        speak("I am at your service. Please tell me how can i help you today?")
    elif hour >=18 and hour<21:
        speak("Good evening sir")
        speak("the current time is "+time())
        time()
        speak("the current date is " +date()[0] + " " + date()[1] + " " + date()[2])
        date()
        speak("I am at your service. Please tell me how may i help you this evening?")
    
    

wishme()
query()