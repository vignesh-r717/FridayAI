import os
import subprocess

SEARCH_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
]


def open_installed_app(app_name):

    app_name = app_name.lower()

    for folder in SEARCH_PATHS:

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.endswith(".lnk"):

                    if app_name in file.lower():

                        path = os.path.join(root, file)

                        os.startfile(path)

                        return f"Opening {file[:-4]}."

    return None