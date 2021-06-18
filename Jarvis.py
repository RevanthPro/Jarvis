#import
import pyttsx3          #Text to speech
import datetime             #To get information about current time and date etc.
import speech_recognition as sr       #Allows Jarvis to recognize what we are speaking
import wikipedia         #Allows Jarvis to search in wikipedia
import webbrowser           #Allows Jarvis to open websites
import os            #Allows Jarvis to manage files in the computer
import sys              #Allows Jarvis to interact with code itself

#Setting the engine
engine = pyttsx3.init('sapi5')                 #Setting the voice engine to pyttsx3
voices = engine.getProperty('voices')                   #assigning the property 'voices' to variable voices
engine.setProperty('voice', voices[0].id)                      #Setting the voice to female voice

#Functions
def speak(audio):
    '''This function allows Jarvis to speak with 
        the help of argument audio.This function 
        uses a basic function called say which 
        comes with pyttsx3'''
    
    engine.say(audio)               #Take the argument audio and says it out
    engine.runAndWait()                 #Makes the code run until it completes saying the audio


def wishMe():
    '''This function allows Jarvis to wish
        user by knowing the time using the
        datetime module and checking if it's
        morning or afternoon or evening.
        This depends on speak function
        written above'''
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Jarvis. How can I help you?")


def takeCommand():
    '''This function takes audio from the user
        and uses google to recognize what the 
        user said and prints what the user said'''
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query
    



#Main code
if __name__ == '__main__':
    wishMe()
    
    #loops
    while True:
        query = takeCommand().lower()


    #Allows Jarvis to search in wikipedia
        if 'wikipedia' in query:
            print("Searching wikipedia...")
            speak("Searching wikipedia...")
            query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)


    #Allows Jarvis to open youtube
        elif 'open youtube' in query:
            print("Opening Youtube...")
            speak("Opening Youtube...")
            webbrowser.get().open('http://www.youtube.com')


    #Allows Jarvis to open google
        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.get().open('http://www.google.com')


    #Allows Jarvis to open facebook
        elif 'open facebook' in query:
            print("Opening Facebook...")
            speak("Opening Facebook...")
            webbrowser.get().open('http://www.facebook.com')


    #Allows Jarvis to open twitter
        elif 'open twitter' in query:
            print("Opening twitter...")
            speak("Opening twitter...")
            webbrowser.get().open('http://www.twitter.com')


    #Allows Jarvis to tell the time to the user
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is : {time}")


    #Allows Jarvis to open vscode
        elif 'code' in query:
            print("Opening vscode...")
            speak("Opening vscode...")
            codePath = "C:\\Users\\Revanth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


    #Allows Jarvis to open File Explorer
        elif 'files' in query:
            print("Opening File Explorer...")
            speak("Opening File Explorer...")
            fileExplorerPath = "C:\\"
            os.startfile(fileExplorerPath)


    #Allows Jarvis to open Brave
        elif 'brave' in query:
            print("Opening Brave...")
            speak("Opening Brave...")
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravePath)


    #Allows Jarvis to Stop running code
        elif 'exit' in query:
            print("Exiting...")
            speak("Exiting...")
            sys.exit()