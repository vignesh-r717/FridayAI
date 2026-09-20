from core.voice import listen
from core.brain import think
from core.speaker import speak

print("=" * 40)
print("        FRIDAY AI")
print("=" * 40)
print("Say 'exit' to quit.")
print()

while True:

    command = listen()

    if command == "":
        continue

    if command.lower() in ["exit", "quit", "goodbye"]:
        print("FRIDAY: Goodbye!")
        speak("Goodbye!")
        break

    response = think(command)

    print("\nFRIDAY:", response)

    speak(response)