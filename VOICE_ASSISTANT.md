## Voice AI Conversation Layer for BrowserOS (OpenRouter Version)

### Requirements
- Python 3.8+
- `SpeechRecognition`, `PyAudio`, `pyttsx3`, `requests`, `python-dotenv`
  ```
  pip install SpeechRecognition PyAudio pyttsx3 requests python-dotenv
  ```

### Setup
1. Create a `.env` file in your project root with:
   ```
   OPENROUTER_API_KEY=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
   ```
2. Make sure your microphone is connected.

### Usage
Run:
```
python voice_assistant.py
```
Speak your question. The assistant will reply using voice.  
Say **'quit'** to exit.

### Notes
- Your API key stays private—never expose it in source code!
- Default model: `"openrouter/auto"`, you can specify other models in the code.
