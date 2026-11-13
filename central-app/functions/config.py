"""Load and edit the settings shared by the central app and its config window."""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")


def load_config(defaults=None):
    """Read settings, falling back to defaults for missing or invalid values."""
    settings = dict(defaults or {})
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as config_file:
            saved = json.load(config_file)
        if isinstance(saved, dict):
            settings.update(saved)
    except (OSError, json.JSONDecodeError):
        pass
    return settings


def save_config(settings):
    """Persist shared settings to config.json."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as config_file:
        json.dump(settings, config_file, indent=4, ensure_ascii=False)


def open_config_window():
    # Imports stay here so app.py can load settings without creating a second
    # Tk window or initializing another speech engine.
    import tkinter as tk
    from tkinter import ttk
    import pyttsx3

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    voice_names = [voice.name for voice in voices]
    voice_ids = {voice.name: voice.id for voice in voices}
    current_voice_id = engine.getProperty("voice")
    default_voice_name = next(
        (voice.name for voice in voices if voice.id == current_voice_id),
        voice_names[0] if voice_names else "",
    )
    defaults = {
        "voice": default_voice_name,
        "voice_id": current_voice_id,
        "rate": 200,
        "volume": 1.0,
    }
    config = load_config(defaults)

    root = tk.Tk()
    root.title("Configurações")
    root.geometry("400x300")
    root.resizable(False, False)

    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)

    tk.Label(main_frame, text="Voz:", font=("Arial", 12)).pack(anchor="w")
    voice_var = tk.StringVar(value=config.get("voice", default_voice_name))
    voice_combo = ttk.Combobox(
        main_frame,
        textvariable=voice_var,
        values=voice_names,
        state="readonly",
        width=40,
    )
    voice_combo.pack(pady=(5, 15), fill="x")

    tk.Label(main_frame, text="Velocidade da fala:", font=("Arial", 12)).pack(anchor="w")
    rate_var = tk.IntVar(value=config.get("rate", 200))
    rate_scale = tk.Scale(main_frame, from_=50, to=500, orient="horizontal", variable=rate_var)
    rate_scale.pack(pady=(0, 15), fill="x")

    tk.Label(main_frame, text="Volume:", font=("Arial", 12)).pack(anchor="w")
    volume_var = tk.DoubleVar(value=config.get("volume", 1.0))
    volume_scale = tk.Scale(
        main_frame,
        from_=0.0,
        to=1.0,
        resolution=0.1,
        orient="horizontal",
        variable=volume_var,
    )
    volume_scale.pack(pady=(0, 20), fill="x")

    def save_and_close():
        selected_voice = voice_var.get()
        save_config(
            {
                "voice": selected_voice,
                "voice_id": voice_ids.get(selected_voice, current_voice_id),
                "rate": rate_var.get(),
                "volume": round(volume_var.get(), 2),
            }
        )
        root.destroy()

    tk.Button(main_frame, text="Salvar", font=("Arial", 12), width=15, command=save_and_close).pack()
    root.mainloop()


if __name__ == "__main__":
    open_config_window()
