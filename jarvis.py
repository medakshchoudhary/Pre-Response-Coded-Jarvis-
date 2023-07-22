import pyttsx3
import speech_recognition as sr
import datetime
import Wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('vioce', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Please tell me How may i help u")

    taskexecution()

def takecommand(ask = False):
    # It takes microphone input from the user and returns string outut

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        if ask:
            print(ask)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please..")    
        speak("Say that again please..")
        return "None"  
         
    return query.lower()    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ch.daksh01@gmail.com', 'dakshnrehaan.01')
    server.sendmail('ch.daksh01@gmail.com', to, content)
    server.close()

def taskexecution():
    while True:
        query = takecommand()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
        
        if 'search' in query:
            speak("what do you want me to search for")
            search = takeCommand()
            url = "https://google.com/search?q=" + search
            webbrowser.get().open(url)
            speak("Heres what i found for u sir!" + search)
            
        if 'find a location' in query:
            speak("which location do u want me find for u sir!")
            location = takecommand()
            url = "https://google.nl/maps/place/" + location + '/&amp;'
            webbrowser.get().open(url)
            speak("Heres the location which u were looking for sir" + location)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube...")

        elif 'open google' in query:
            webbrowser.open("google.com") 
            speak("Opening google...")  

        elif 'open chrome' in query:
            codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
            speak("Opening chrome...")
            os.startfile(codepath)

        elif 'play akh lad jaave' in query:
            music_dir = "C:\\Users\\chdak\\Desktop\\Jarvis muisc TEST\\akh lad jaave"
            speak("heres one for u sir! also mine favourite. droping the beat for u")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
                    
        elif 'time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\chdak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening my birthplace sir")
            os.startfile(codepath)
            
        elif 'hello' in query:
            speak("hello sir")

        elif 'play memories' in query:
            music_dir = "C:\\Users\\chdak\\Desktop\\Jarvis muisc TEST\\memories"
            speak("heres one for u sir! also mine favourite. droping the beat for u")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play for you' in query:
            music_dir = "C:\\Users\\chdak\\Desktop\\Jarvis muisc TEST\\for you"
            speak("heres one for u sir! also mine favourite. droping the beat for u")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))    

        elif 'open cmd' in query:
            codepath = "C:\\Windows\\System32\\cmd.exe"
            speak("opening cmd..")
            os.startfile(codepath)
           
        elif 'email to sanvi' in query:
            try:
                speak("What should i say sir")
                content = takecommand()
                to = "queensaanvi1807@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir I was not able to send the email at the moment")

        elif 'email to vikas' in query:
            try:
                speak("What should i say sir")
                content = takecommand()
                to = "watersofchinab@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir I was not able to send the email at the moment")

        elif 'email to anita' in query:
            try:
                speak("What should i say sir")
                content = takecommand()
                to = "aintadogra75@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir I was not able to send the email at the moment")
                
        elif 'thanks' in query:
            speak("welcome sir")

        elif 'what is my name' in query:
            speak("your name is daksh")

        elif 'bye' in query or 'bye bye' in query:
            speak("bye sir have a nice day")    
            break

        elif 'have a nice day jarvis' in query:
            speak("you 2 sir")
            break

        elif 'exit' in query:
            speak("have a nice day sir")
            break

        else:
            if '' in query or 'what' in query or 'how' in query or 'where' in query or 'when' in query:
                query = query.replace("jarvis" ,"")


if __name__ == "__main__":
    permission = takecommand()

    while True:

        if "jarvis" in query or "wake up jarvis" in permission:
            wishme()

    


    
            

            