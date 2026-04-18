from context_detector import detect_context

def run_tests():
    samples = [
        "i feel sad",
        "i have exam tomorrow",
        "i cant focus",
        "lets talk"
    ]

    for text in samples:
        intent, mood = detect_context(text)
        print(f"Input: {text}")
        print(f"Intent: {intent}, Mood: {mood}")
        print("-" * 30)

if __name__ == "__main__":
    run_tests()