import datetime
import os
import smtplib
import time
import webbrowser
import pyautogui as pyautogui
import pyjokes as pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia as wikipedia
from tkinter import *


root = Tk()
root.title("Alexa")
root.geometry("1920x1080")


a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()


def take_command():
    ram = sr.Recognizer()
    with sr.Microphone() as mic:
        a.set("HELLO SHREYANSH....")
        pyttsx3.speak("Hello SHREYANSH.....")
        ram.pause_threshold = 1
        audio = ram.listen(mic)
        vr = ram.recognize_google(audio, language='en-in')
        vr = vr.lower()
        b.set(vr)
        if "wikipedia" in vr:
            c.set("Searching on wikipedia")
            pyttsx3.speak("Searching on wikipedia")
            vr = vr.replace("wikipedia", " ")
            result = wikipedia.summary(vr, sentences=3)
            d.set(result)
            pyttsx3.speak(result)
        elif "open google" in vr:
            print("Opening Google")
            pyttsx3.speak("Opening Google")
            webbrowser.open("www.google.com")
        elif "open youtube" in vr:
            print("Opening Youtube")
            pyttsx3.speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
        elif "in google" in vr:
            vr = vr.replace("in google", " ")
            vr = vr.replace("search", " ")
            print(f"Searching {vr}")
            pyttsx3.speak(f"Searching {vr}")
            webbrowser.open(f"https://www.google.co.in/search?q={vr}")
        elif "in youtube" in vr:
            vr = vr.replace("in youtube", " ")
            vr = vr.replace("search", " ")
            print(f"Searching {vr}")
            pyttsx3.speak(f"Searching {vr}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={vr}")
        elif "tell me a joke" in vr:
            ans = pyjokes.get_joke()
            print(ans)
            pyttsx3.speak(ans)
        elif "time" in vr:
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            pyttsx3.speak(datetime.datetime.now().strftime("%H:%M:%S"))
        elif "open ms word" in vr:
            print("Opening MS word")
            pyttsx3.speak("Opening MS word")
            path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk"
            os.startfile(path)
        # "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk"

        elif "screenshot" in vr:
            print("Tell me the name of the file you want to take screenshot in.")
            pyttsx3.speak("Tell me the name of the file you want to take screenshot in.")
            ram = sr.Recognizer()
            with sr.Microphone() as source:
                ram.pause_threshold = 1
                audio = ram.listen(source)
                print(audio)
                query = ram.recognize_google(audio, language='en-in')
                query = query.lower()
            print("Hold the screen for few seconds")
            pyttsx3.speak("Hold the screen for few seconds")
            time.sleep(1)
            img = pyautogui.screenshot()
            img.save(f"E:/{query}.png")
            print("Screenshot saved successfully")
            pyttsx3.speak("Screenshot saved successfully")
        elif "switch" in vr:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "unstoppable" in vr:
            pyttsx3.speak("Playing Unstoppable")
            c.set("Playing Unstoppable")
            os.startfile("E:\songs\\a.mp3")

        elif "radioactive" in vr:
            pyttsx3.speak("Playing Radioactive")
            c.set("Playing Radioactive")
            os.startfile("E:\songs\\c.mp3")

        elif "girls like you" in vr:
            pyttsx3.speak("Playing Girls like you")
            c.set("Playing Girls like you")
            os.startfile("E:\songs\\b.mp3")

        elif "open turbo c plus plus" in vr:
            print("Opening Turbo C++")
            pyttsx3.speak("Opening Turbo C plus plus")
            path = r"C:\Users\Public\Desktop\Turbo C++.lnk"
            os.startfile(path)

        elif "open microsoft teams" in vr:
            print("Opening Microsoft Teams")
            pyttsx3.speak("Opening Microsoft Teams")
            path = r"C:\Users\lenovo\Desktop\Microsoft Teams.lnk"
            os.startfile(path)

        elif "google maps" in vr:
            print("Opening Google Maps")
            pyttsx3.speak("Opening Google Maps")
            start = vr.replace("search", " ")
            start = start.replace("on google maps", " ")
            url = "https://www.google.com/maps/place/" + start
            webbrowser.open(url)

        elif "email myself" in vr:
            pyttsx3.speak("What should I say")
            print("What should I say")
            content = take_command()
            print(content)
            to = "shreyansh.jain251202@gmail.com"
            send_mail(to, content)

        elif "open command prompt" in vr:
            print("Opening command prompt")
            pyttsx3.speak("Opening command prompt")
            os.system("start cmd")

        elif "ip address" in vr:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            pyttsx3.speak(ip)


def send_mail(to, content):
    server = smtplib.SMTP("sntp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("shreyansh.jain251202@gmail.com", "")
    server.sendmail("shreyansh.jain251202@gmail.com", to, content)
    server.close()


e = PhotoImage(file="alexaa.png")
img = Label(root, image=e)
img.place(x=0, y=0)

ans1 = Entry(root, font="Arial 15 bold", fg="black", textvariable=a)
ans1.place(x=10, y=150, width=500)

ans2 = Entry(root, font="Arial 15 bold", fg="black", textvariable=b)
ans2.place(x=10, y=250, width=500)

ans3 = Entry(root, font="Arial 15 bold", fg="black", textvariable=c)
ans3.place(x=10, y=350, width=500)

ans4 = Entry(root, font="Arial 15 bold", fg="black", textvariable=d)
ans4.place(x=10, y=450, width=500)

alexapp = Button(root, font="Arial 15 bold", text="Alexa", command=take_command)
alexapp.place(x=950, y=640)

root.mainloop()

