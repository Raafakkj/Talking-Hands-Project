import os
import json
import tkinter as tk
from tkinter import ttk
import pyttsx3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_names = [v.name for v in voices]
voice_ids = {v.name: v.id for v in voices}

default_voice_id = engine.getProperty('voice')
default_voice_name = next((v.name for v in voices if v.id == default_voice_id), voice_names[0] if voice_names else "")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "voice": default_voice_name,
        "voice_id": default_voice_id,
        "rate": 200,
        "volume": 1.0
    }

def save_config():
    data = {
        "voice": voice_var.get(),
        "voice_id": voice_ids.get(voice_var.get(), default_voice_id),
        "rate": rate_var.get(),
        "volume": round(volume_var.get(), 2)
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    root.destroy()

config = load_config()

root = tk.Tk()
root.title("Configurações")
root.geometry("400x300")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

tk.Label(main_frame, text="Voz:", font=("Arial", 12)).pack(anchor="w")
voice_var = tk.StringVar(value=config.get("voice", default_voice_name))
voice_combo = ttk.Combobox(main_frame, textvariable=voice_var, values=voice_names, state="readonly", width=40)
voice_combo.pack(pady=(5, 15), fill="x")

tk.Label(main_frame, text="Velocidade da fala:", font=("Arial", 12)).pack(anchor="w")
rate_var = tk.IntVar(value=config.get("rate", 200))
rate_scale = tk.Scale(main_frame, from_=50, to=500, orient="horizontal", variable=rate_var)
rate_scale.pack(pady=(0, 15), fill="x")

tk.Label(main_frame, text="Volume:", font=("Arial", 12)).pack(anchor="w")
volume_var = tk.DoubleVar(value=config.get("volume", 1.0))
volume_scale = tk.Scale(main_frame, from_=0.0, to=10.0, resolution=0.1, orient="horizontal", variable=volume_var)
volume_scale.pack(pady=(0, 20), fill="x")

save_button = tk.Button(main_frame, text="Salvar", font=("Arial", 12), width=15, command=save_config)
save_button.pack()

root.mainloop()