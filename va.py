import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()                                                                                                                        
def wishme():                                                                           
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good Afternoon sir")
    else:
        speak("good evening sir")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            #print(e)   
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        
        return query
 
if __name__=="__main__" :
    wishme()
    speak("how may i help you")
    while (1):
        query=takeCommand().lower()
        if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open('https://wynk.in/u/youIsJanw')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'quit' in query:
            break     
 





