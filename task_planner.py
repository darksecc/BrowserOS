import requests
import json

def plan_task(user_command, openai_key):
    prompt = (
        "You are BrowserOS AI, an assistant with full browser powers. Based on the following user command, break the desired action into clear, step-by-step browser tasks as a JSON array ('action', 'parameters'). After the JSON, reply with a short summary for the user.\n"
        f"User command: {user_command}\n"
        "Example output:\n"
        "[{\"action\": \"open_url\", \"parameters\": {\"url\": \"https://github.com\"}}, {\"action\": \"search\", \"parameters\": {\"query\": \"AI news\"}}]\nSummary: I will open GitHub and search for AI news."
    )
    headers = {
        "Authorization": f"Bearer {openai_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/darksecc/BrowserOS",
        "X-Title": "BrowserOS Task Planner"
    }
    messages = [
        {"role": "system", "content": "You output JSON steps and then a short summary."},
        {"role": "user", "content": prompt}
    ]
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json={"model": "openrouter/auto", "messages": messages}
    )
    data = response.json()
    response_text = data["choices"][0]["message"]["content"]
    # Parse response: [JSON array]\nSummary
    try:
        json_section = response_text.split("\n")[0]
        steps = json.loads(json_section)
        summary = "\n".join(response_text.split("\n")[1:]).strip()
    except Exception as e:
        steps = []
        summary = "Could not parse task plan."
    return steps, summary
