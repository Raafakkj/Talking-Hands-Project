import os
import sys
import tkinter as tk
from tkinter import PhotoImage, Label, Button
import pyttsx3
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.title("Central App")
root.geometry("800x600")
engine = pyttsx3.init()
engine.setProperty('volume', 5.0)

user_input = ""
voices = engine.getProperty('voices')
for voice in voices:
    if 'portuguese' in voice.name.lower() or 'brazil' in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

image_path = os.path.join(BASE_DIR, "assets", "botao-de-configuracoes-de-preto.png")
config_image = PhotoImage(file=image_path)

def entry_reader():
    global user_input
    user_input = entry.get()
    engine.say(user_input)
    engine.runAndWait()

def open_config():
    config_script = os.path.join(BASE_DIR, "functions", "config.py")
    subprocess.Popen([sys.executable, config_script])

top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=15, pady=10)

config_button = tk.Button(top_frame, image=config_image, command=open_config, bd=0)
config_button.pack(side="right")

center_frame = tk.Frame(root)
center_frame.pack(expand=True)

entry = tk.Entry(center_frame, width=40, font=("Arial", 18))
entry.pack(pady=(0, 15), padx=20)

button = tk.Button(center_frame, text="Submit", font=("Arial", 14), width=15, command=entry_reader)
button.pack()

root.mainloop()