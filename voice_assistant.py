import speech_recognition as sr
import pyttsx3
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Say something:")
    with mic as source:
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def ai_respond(prompt, conversation_history):
    conversation_history.append({"role": "user", "content": prompt})
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/darksecc/BrowserOS",
        "X-Title": "BrowserOS Voice Assistant"
    }
    data = {
        "model": "openrouter/auto",
        "messages": conversation_history
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    try:
        result = response.json()
        msg = result["choices"][0]["message"]["content"].strip()
        conversation_history.append({"role": "assistant", "content": msg})
        return msg
    except Exception as e:
        return f"Error: {e}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    if not OPENROUTER_API_KEY:
        print("OpenRouter API Key not set. Please set it in your .env file.")
        exit(1)
    conversation_history = [
        {"role": "system", "content": "You are a helpful voice assistant."}
    ]
    print("Start speaking. Say 'quit' to exit.")
    while True:
        text = recognize_speech()
        if not text:
            print("Didn't catch that. Try again.")
            continue
        print("You said:", text)
        if text.lower() == "quit":
            print("Goodbye!")
            speak("Goodbye!")
            break
        response = ai_respond(text, conversation_history)
        print("Assistant:", response)
        speak(response)
