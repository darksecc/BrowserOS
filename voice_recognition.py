import speech_recognition as sr

def recognize_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"API error: {e}")

if __name__ == "__main__":
    recognize_from_microphone()
