import customtkinter as ctk
import psutil
import datetime
import threading

from core.brain import think
from core.speaker import speak
from core.assistant import start_assistant
from assets.orb import AIOrb

# -----------------------------
# Window
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🤖 FRIDAY AI")
app.geometry("1000x650")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=4)
app.grid_rowconfigure(0, weight=1)

assistant_running = False

# -----------------------------
# Sidebar
# -----------------------------
sidebar = ctk.CTkFrame(app, width=220)
sidebar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

# -----------------------------
# Main Area
# -----------------------------
main = ctk.CTkFrame(app)
main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
# -----------------------------
# AI Orb
# -----------------------------
orb = AIOrb(main)
orb.pack(pady=15)

# -----------------------------
# Sidebar Widgets
# -----------------------------
title = ctk.CTkLabel(
    sidebar,
    text="🤖 FRIDAY AI",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

status = ctk.CTkLabel(
    sidebar,
    text="🟢 Status : Ready",
    font=("Arial", 18)
)
status.pack(pady=10)

clock = ctk.CTkLabel(
    sidebar,
    text="",
    font=("Arial", 16)
)
clock.pack(pady=5)

system = ctk.CTkLabel(
    sidebar,
    text="",
    font=("Arial", 16)
)
system.pack(pady=5)

# -----------------------------
# Chat Box
# -----------------------------
chat = ctk.CTkTextbox(
    main,
    width=700,
    height=420,
    font=("Consolas", 15)
)
chat.pack(pady=20)

chat.insert(
    "end",
    "🤖 Welcome to FRIDAY AI!\n"
    "Click 🎤 Start to begin voice conversation.\n\n"
)

# -----------------------------
# Input
# -----------------------------
entry = ctk.CTkEntry(
    main,
    width=600,
    placeholder_text="Ask FRIDAY anything..."
)
entry.pack(pady=10)

# -----------------------------
# Chat Helper
# -----------------------------
def add_message(sender, message):
    chat.insert("end", f"{sender}: {message}\n")
    chat.see("end")

# -----------------------------
# Text Chat
# -----------------------------
def send():

    question = entry.get().strip()

    if question == "":
        return

    add_message("🧑 You", question)

    status.configure(text="🧠 Status : Thinking...")
    app.update()

    answer = think(question)

    add_message("🤖 FRIDAY", answer)

    status.configure(text="🔊 Status : Speaking...")

    speak(answer)

    status.configure(text="🟢 Status : Ready")

    entry.delete(0, "end")

# -----------------------------
# Voice Assistant
# -----------------------------
def gui_status(text):
    status.configure(text=text)

def start_voice():

    global assistant_running

    if assistant_running:
        return

    assistant_running = True

    threading.Thread(
        target=start_assistant,
        args=(
            add_message,
            gui_status,
            lambda: assistant_running
        ),
        daemon=True
    ).start()

def stop_voice():

    global assistant_running

    assistant_running = False

    add_message("🤖 FRIDAY", "Voice assistant stopped.")

    status.configure(text="🔴 Status : Stopped")

# -----------------------------
# Buttons
# -----------------------------
button_frame = ctk.CTkFrame(
    main,
    fg_color="transparent"
)
button_frame.pack(pady=10)

send_button = ctk.CTkButton(
    button_frame,
    text="Send",
    command=send,
    width=120
)
send_button.grid(row=0, column=0, padx=8)

voice_button = ctk.CTkButton(
    button_frame,
    text="🎤 Start",
    command=start_voice,
    width=120
)
voice_button.grid(row=0, column=1, padx=8)

stop_button = ctk.CTkButton(
    button_frame,
    text="⏹ Stop",
    command=stop_voice,
    fg_color="red",
    hover_color="#990000",
    width=120
)
stop_button.grid(row=0, column=2, padx=8)

# -----------------------------
# Enter Key
# -----------------------------
entry.bind("<Return>", lambda event: send())

# -----------------------------
# Clock + CPU + RAM
# -----------------------------
def update_system():

    now = datetime.datetime.now().strftime("%I:%M:%S %p")

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    clock.configure(text=f"🕒 {now}")

    system.configure(
        text=f"💻 CPU : {cpu}%\n🧠 RAM : {ram}%"
    )

    app.after(1000, update_system)

update_system()

app.mainloop()