import os
import subprocess
import webbrowser

COMMON_APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "vscode": os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
    "powershell": "powershell",
    "explorer": "explorer",
}


def open_app(app_name):

    app = app_name.lower().strip()

    if app in COMMON_APPS:

        target = COMMON_APPS[app]

        try:

            if target.endswith(".exe"):

                os.startfile(target)

            else:

                subprocess.Popen(target)

            return f"Opening {app_name.title()}."

        except Exception as e:

            return f"Couldn't open {app_name}. {e}"

    try:

        subprocess.Popen(app)

        return f"Opening {app_name.title()}."

    except:

        pass

    webbrowser.open(f"https://www.google.com/search?q={app_name}")

    return f"I couldn't find {app_name}, so I searched it on Google."