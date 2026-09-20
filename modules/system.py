import os
import pyautogui
import screen_brightness_control as sbc


def take_screenshot():

    os.makedirs("screenshots", exist_ok=True)

    filename = "screenshots/screenshot.png"

    pyautogui.screenshot(filename)

    return f"Screenshot saved to {filename}"


def brightness_up():

    try:
        value = sbc.get_brightness()[0]
        sbc.set_brightness(min(value + 10, 100))
        return "Brightness increased."
    except:
        return "Couldn't change brightness."


def brightness_down():

    try:
        value = sbc.get_brightness()[0]
        sbc.set_brightness(max(value - 10, 0))
        return "Brightness decreased."
    except:
        return "Couldn't change brightness."


def set_brightness(level):

    try:
        sbc.set_brightness(level)
        return f"Brightness set to {level}%"
    except:
        return "Couldn't set brightness."


def shutdown():

    os.system("shutdown /s /t 1")

    return "Shutting down."


def restart():

    os.system("shutdown /r /t 1")

    return "Restarting."


def sleep():

    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    return "Sleeping."


def lock_pc():

    os.system("rundll32.exe user32.dll,LockWorkStation")

    return "Locking PC."