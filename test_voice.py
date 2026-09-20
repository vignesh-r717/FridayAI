import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Listening... Speak now.")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)

print("🧠 Recognizing...")

try:
    text = recognizer.recognize_google(audio)
    print("✅ You said:", text)
except sr.UnknownValueError:
    print("❌ Sorry, I couldn't understand you.")
except sr.RequestError as e:
    print("❌ Could not connect:", e)