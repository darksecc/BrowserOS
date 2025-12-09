## Basic Voice Recognition for BrowserOS

### Requirements
- Python 3.8+
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/):  
  ```
  pip install SpeechRecognition
  ```
- [PyAudio](https://pypi.org/project/PyAudio/) (for microphone access):  
  ```
  pip install PyAudio
  ```
  *On some systems, PyAudio may require additional dependencies (see [PyAudio installation guide](https://people.csail.mit.edu/hubert/pyaudio/)).*

### Usage

1. Connect a microphone to your system.
2. Run:
   ```
   python voice_recognition.py
   ```
3. Speak when prompted. The system will print the recognized text to the console.

### Notes

- This uses [Google Web Speech API](https://cloud.google.com/speech-to-text) via the SpeechRecognition package for simple, local prototyping.
- For accurate and production use, consider handling API limits and using offline/other engines.
