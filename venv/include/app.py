import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Привет")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("You say: " + str(command))

    except sr.UnknownValueError:
        talk("I don't understand you")
        zadanie = command()

    return zadanie

def makeSomething(zadanie):
    if 'super' in zadanie:
        talk("Already opening")
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk('Yes, of course')
        sys.exit()
    elif 'name' in zadanie:
        talk("My name is Siri")

while True:
    makeSomething(command())