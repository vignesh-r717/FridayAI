import os
import webbrowser
import subprocess

# ------------------------
# Desktop Apps
# ------------------------

def open_notepad():
    os.system("notepad")


def open_calculator():
    os.system("calc")


def open_chrome():
    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.path.exists(chrome):
        os.startfile(chrome)
    else:
        webbrowser.open("https://google.com")


def open_vscode():
    vscode = os.path.expandvars(
        r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    )

    if os.path.exists(vscode):
        os.startfile(vscode)
    else:
        print("VS Code not found.")


def open_explorer():
    subprocess.Popen("explorer")


def open_downloads():
    path = os.path.join(os.path.expanduser("~"), "Downloads")
    os.startfile(path)


def open_documents():
    path = os.path.join(os.path.expanduser("~"), "Documents")
    os.startfile(path)


# ------------------------
# Websites
# ------------------------

def open_youtube():
    webbrowser.open("https://youtube.com")


def open_google():
    webbrowser.open("https://google.com")


def open_chatgpt():
    webbrowser.open("https://chatgpt.com")


def open_github():
    webbrowser.open("https://github.com")


def open_gmail():
    webbrowser.open("https://mail.google.com")


# ------------------------
# Search
# ------------------------

def google_search(query):
    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )


def youtube_search(query):
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )