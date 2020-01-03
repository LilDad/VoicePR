import speech_recognition as sr
import os
import sys
import webbrowser

# Функция воспроизведения текста
def talk(words):
    print(words)
    os.system("Say " + words)

talk("Hi. Ask me something.")

# Функция для прослушки
def command():
    r = sr.Recognizer()

    # Активация микрофона с паузой
    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1

        # Отсекание фона
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("You say: " + zadanie)
    # Исключение ошибки
    except sr.UnknownValueError:
        talk("I don't understand you.")

    return zadanie