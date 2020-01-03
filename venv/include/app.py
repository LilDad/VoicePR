import speech_recognition as sr
import os
import sys
import webbrowser

# Функция воспроизведения текста
def talk(words):
    print(words)
    os.system("Say " + words)

talk("Hi. Ask me something.")

