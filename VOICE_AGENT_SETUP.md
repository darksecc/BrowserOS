# BrowserOS AI Voice Agent (Jarvis-like)

## How to Run

1. Ensure you have your `.env` file with:
   ```
   OPENROUTER_API_KEY=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
   ```
2. Install dependencies:
   ```
   pip install SpeechRecognition PyAudio pyttsx3 requests python-dotenv
   ```
3. Run it:
   ```
   python voice_agent.py
   ```
4. Speak your task or command!
   - The AI will plan in steps.
   - Actions will be confirmed aloud.

## Notes
- Real browser action execution requires calling BrowserOS APIs inside `executor.py` (stubbed for demo).
- The system is modular: swap out planner, executor, or integrate deeper!
