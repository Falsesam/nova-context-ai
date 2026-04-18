def detect_context(user_input):
    text = user_input.lower()

    # intent detection
    if any(word in text for word in ["study", "exam", "learn", "understand"]):
        intent = "study"
    elif any(word in text for word in ["sad", "stress", "tired", "upset", "lonely","left out","burn out",]):
        intent = "emotional"
    elif any(word in text for word in ["work", "focus", "task", "productive","deadline","assignment","project"]):
        intent = "productivity"
    else:
        intent = "casual"

    # Mood detection
    if any(word in text for word in ["sad", "depressed", "down"]):
        mood = "sad"
    elif any(word in text for word in ["confused", "don't understand", "lost"]):
        mood = "confused"
    elif any(word in text for word in ["motivated", "excited", "ready"]):
        mood = "motivated"
    else:
        mood = "neutral"

    return intent, mood