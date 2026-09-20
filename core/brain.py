from modules.memory import remember, recall
from core.ai import ask_ai
from core.router import handle


def think(command):

    command = command.strip()
    lower = command.lower()

    # ------------------------
    # Memory
    # ------------------------

    if lower.startswith("my name is "):
        name = command[11:]
        remember("name", name)
        return f"Nice to meet you, {name}!"

    elif lower == "what is my name":
        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."

    # ------------------------
    # Router
    # ------------------------

    handled, response = handle(command)

    if handled:
        return response

    # ------------------------
    # AI
    # ------------------------

    return ask_ai(command)