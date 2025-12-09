import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from task_planner import plan_task
from executor import execute_task

load_dotenv()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening for command...")
    with mic as source:
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception:
        return ""

if __name__ == "__main__":
    openai_key = os.getenv("OPENROUTER_API_KEY")
    if not openai_key:
        print("Missing OpenRouter API Key in .env")
        exit(1)
    speak("Hello! I am BrowserOS AI. How can I assist you today?")
    while True:
        cmd = recognize_speech()
        if not cmd:
            speak("Didn't catch that, please try again.")
            continue
        print("You said:", cmd)
        if cmd.lower() in ["quit", "exit"]:
            speak("Goodbye!")
            break
        task_plan, agent_response = plan_task(cmd, openai_key)
        speak(agent_response)
        print("Planned tasks:", task_plan)
        for task in task_plan:
            result = execute_task(task)
            speak(result)
            print("Result:", result)
