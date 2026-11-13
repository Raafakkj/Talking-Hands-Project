import os
import sys
import tkinter as tk
from tkinter import PhotoImage
import pyttsx3
import subprocess
from functions.config import load_config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.title("Central App")
root.geometry("800x600")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_ids_by_name = {voice.name: voice.id for voice in voices}
default_voice_id = engine.getProperty('voice')
default_voice_name = next(
    (voice.name for voice in voices if voice.id == default_voice_id),
    voices[0].name if voices else "",
)
settings = load_config(
    {"voice": default_voice_name, "voice_id": default_voice_id, "rate": 200, "volume": 1.0}
)


def apply_config():
    """Apply the saved speech settings to the app's engine."""
    selected_voice_id = settings.get("voice_id") or voice_ids_by_name.get(settings.get("voice"))
    available_voice_ids = {voice.id for voice in voices}
    if selected_voice_id in available_voice_ids:
        engine.setProperty("voice", selected_voice_id)
    engine.setProperty("rate", int(settings.get("rate", 200)))
    engine.setProperty("volume", max(0.0, min(1.0, float(settings.get("volume", 1.0)))))


apply_config()
user_input = ""
config_process = None

image_path = os.path.join(BASE_DIR, "assets", "botao-de-configuracoes-de-preto.png")
config_image = PhotoImage(file=image_path)

def entry_reader():
    global user_input
    user_input = entry.get()
    if not user_input.strip():
        return

    engine.say(user_input)
    engine.runAndWait()

def open_config():
    global config_process
    if config_process is not None and config_process.poll() is None:
        return
    config_script = os.path.join(BASE_DIR, "functions", "config.py")
    config_process = subprocess.Popen([sys.executable, config_script], cwd=BASE_DIR)
    check_config_closed()


def check_config_closed():
    if config_process is not None and config_process.poll() is None:
        root.after(200, check_config_closed)
        return
    settings.update(load_config(settings))
    apply_config()

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
