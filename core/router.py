from datetime import datetime

from modules.apps import *
from modules.app_launcher import open_app
from modules.weather import get_weather
from modules.system import *
from modules.volume import *
from modules.app_scanner import open_installed_app


def handle(command):

    lower = command.lower().strip()

    # ------------------------
    # Time
    # ------------------------

    if "time" in lower:
        return True, f"The time is {datetime.now().strftime('%I:%M %p')}"

    # ------------------------
    # Date
    # ------------------------

    if "date" in lower:
        return True, f"Today is {datetime.now().strftime('%d %B %Y')}"

    # ------------------------
    # Weather
    # ------------------------

    if (
        "weather" in lower
        or "rain" in lower
        or "temperature" in lower
        or lower == "hot"
        or lower == "cold"
    ):

        city = "Coimbatore"

        if " in " in lower:
            city = command.split(" in ", 1)[1]

        return True, get_weather(city)

    # ------------------------
    # Google Search
    # ------------------------

    if lower.startswith("search google for "):

        query = command[18:]

        google_search(query)

        return True, f"Searching Google for {query}"

    # ------------------------
    # YouTube Search
    # ------------------------

    if lower.startswith("search youtube for "):

        query = command[19:]

        youtube_search(query)

        return True, f"Searching YouTube for {query}"

    if lower.startswith("play "):

        query = command[5:]

        youtube_search(query)

        return True, f"Playing {query}"

    # ------------------------
    # Built-in Apps
    # ------------------------

    if lower == "open notepad":
        open_notepad()
        return True, "Opening Notepad."

    if lower == "open calculator":
        open_calculator()
        return True, "Opening Calculator."

    if lower == "open chrome":
        open_chrome()
        return True, "Opening Chrome."

    if lower == "open vscode":
        open_vscode()
        return True, "Opening VS Code."

    if lower == "open youtube":
        open_youtube()
        return True, "Opening YouTube."

    if lower == "open google":
        open_google()
        return True, "Opening Google."

    if lower == "open github":
        open_github()
        return True, "Opening GitHub."

    if lower == "open gmail":
        open_gmail()
        return True, "Opening Gmail."

    if lower == "open chatgpt":
        open_chatgpt()
        return True, "Opening ChatGPT."

    if lower == "open file explorer":
        open_explorer()
        return True, "Opening File Explorer."

    if lower == "open downloads":
        open_downloads()
        return True, "Opening Downloads."

    if lower == "open documents":
        open_documents()
        return True, "Opening Documents."

    # ------------------------
    # Open Any Installed App
    # ------------------------

    if lower.startswith("open "):

        app = command[5:]

        result = open_installed_app(app)

        if result:
            return True, result

        return True, open_app(app)

    # ------------------------
    # Screenshot
    # ------------------------

    if "screenshot" in lower:
        return True, take_screenshot()

    # ------------------------
    # Brightness
    # ------------------------

    if "brightness up" in lower:
        return True, brightness_up()

    if "brightness down" in lower:
        return True, brightness_down()

    if lower.startswith("brightness "):

        try:
            level = int(lower.split()[1])
            return True, set_brightness(level)

        except:
            pass

    # ------------------------
    # Volume
    # ------------------------

    if "volume up" in lower:
        return True, volume_up()

    if "volume down" in lower:
        return True, volume_down()

    if lower == "mute":
        return True, mute()

    if lower == "unmute":
        return True, unmute()

    if lower.startswith("volume "):

        try:
            level = int(lower.split()[1])

            if 0 <= level <= 100:
                return True, set_volume(level)

        except:
            pass

    # ------------------------
    # Power
    # ------------------------

    if lower == "shutdown computer":
        return True, shutdown()

    if lower == "restart computer":
        return True, restart()

    if lower == "lock computer":
        return True, lock_pc()

    if lower == "sleep computer":
        return True, sleep()

    return False, None