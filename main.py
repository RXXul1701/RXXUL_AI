
import os
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
from bardapi import Bard
from dotenv import load_dotenv
def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
    print(text)

def AI(prompt):
    load_dotenv()
    token = os.getenv("KEY")
    bard = Bard(token=token)
    result = bard.get_answer(prompt, max_tokens=50)
    speak(result["content"])
    #except Exception as e:(p
        #speak("No prompt given")


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"RAHUL: {query}\nRXXUL A,I: "
    prompt=chatStr
    load_dotenv()
    token = os.getenv("KEY")
    bard = Bard(token=token)
    result = bard.get_answer(prompt)
    speak(result["content"])
    chatStr += f"{result['content']}\n"
    return result["content"]


def takeCommand():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language="en-in")
                print("Recognizing voice..")
                return query
            except Exception as e:
                speak("Pardon sir, could you please repeat what you just said?")
                continue




if __name__=='__main__':
    speak("Hello...I am Rxxul A,I")
    while True:
        print("Listening...")
        query = takeCommand()
        command_executed = False


        sites = [["youtube","https://www.youtube.com/"],
                 ["google","https://www.google.com/"],
                 ["instagram","https://www.instagram.com/"],
                 ["Bing AI","https://www.bing.com/search?form=MY0291&OCID=MY0291&q=Bing+AI&showconv=1"],
                 ["facebook", "https://www.facebook.com/"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                try:
                    speak(f"opening {site[0]} sir...")
                    webbrowser.open(site[1])
                    command_executed = True
                    break
                except Exception as e:
                    speak("No website was asked to open")
        music = [
            ["channa mereya", "C:\\Users\\USER\\Downloads\\Channa Mereya.mp3"],
            ["metamorphosis", "C:\\Users\\USER\\Downloads\\Metamorphosis.mp3"],
            ["make you mine", "C:\\Users\\USER\\Downloads\\Make You Mine.mp3"],
            ["Dancing with your ghost", "C:\\Users\\USER\\Downloads\\Dancing with your ghost.mp3"],
            ["Until I Found You", "C:\\Users\\USER\\Downloads\\Until I Found You.mp3"],
            ["A Thousand Years", "C:\\Users\\USER\\Downloads\\A Thousand Years.mp3"],
            ["Rahogi Meri", "C:\\Users\\USER\\Downloads\\Rahogi Meri.mp3"],
            ["Perfect", "C:\\Users\\USER\\Downloads\\Perfect.mp3"],
            ["Tujhe Kitna Chahne lage", "C:\\Users\\USER\\Downloads\\Tujhe Kitna Chahne Lage.mp3"],
            ["Let Her Go", "C:\\Users\\USER\\Downloads\\Let Her Go.mp3"],
            ["Pehla Nasha", "C:\\Users\\USER\\Downloads\\Pehla Nasha.mp3"]
        ]

        for songs in music:
            if f"play {songs[0]} for me".lower() in query.lower():
                musicpath = songs[1]
                try:
                    speak(f"sure sir, Playing {songs[0]} for you")
                    os.startfile(musicpath)
                    command_executed = True
                    break

                except Exception as e:
                    speak("Sorry bro, error occured")
        if "the time" in query:
            CurrentTime = datetime.datetime.now().strftime("%I:%m%p")
            speak(f"The time is {CurrentTime} ")

        elif "using artificial intelligence".lower() in query.lower():
            AI(prompt=query)

        elif "Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
        if not command_executed:
            print("Chatting...")
            chat(query)





