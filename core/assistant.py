from core.voice import listen
from core.brain import think
from core.speaker import speak


def start_assistant(update_chat, update_status, is_running):

    update_status("🎤 Status : Listening...")

    while is_running():

        command = listen()

        if not is_running():
            break

        if command == "":
            continue

        update_chat("🧑 You", command)

        if command.lower() in ["exit", "quit", "goodbye"]:
            update_chat("🤖 FRIDAY", "Goodbye!")
            speak("Goodbye!")
            update_status("🔴 Status : Stopped")
            break

        update_status("🧠 Status : Thinking...")

        answer = think(command)

        update_chat("🤖 FRIDAY", answer)

        update_status("🔊 Status : Speaking...")

        speak(answer)

        update_status("🎤 Status : Listening...")

    update_status("🔴 Status : Stopped")