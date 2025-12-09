def execute_task(task):
    action = task.get("action")
    params = task.get("parameters", {})
    if action == "open_url":
        # Insert BrowserOS browser API here for actual navigation
        return f"Opening URL: {params.get('url')}"
    elif action == "search":
        return f"Searching: {params.get('query')}"
    elif action == "click":
        return f"Clicking element: {params.get('selector')}"
    elif action == "read":
        return "Reading page content."
    elif action == "speak":
        return params.get("text", "")
    else:
        return "Unknown action"
