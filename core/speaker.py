import asyncio
import edge_tts
import tempfile
import os
from playsound import playsound

VOICE = "en-US-GuyNeural"

async def speak_async(text):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(temp_file.name)

    playsound(temp_file.name)

    os.remove(temp_file.name)

def speak(text):
    asyncio.run(speak_async(text))