"""
Main entry point for NOVA assistant.
"""

import time
import random
from context_detector import detect_context
from prompt_engine import generate_response


def run_chat():
    print("Hi, I'm NOVA - the Context-Aware AI Assistant 🤖")
    print("Type 'end' to end the chat ❤️\n")

    conversation_history = []

    conversation_state = {
        "topic": None,
        "emotion_level": 0
    }

    while True:
        user_input = input("You: ")

        if user_input.lower() == "end":
            print("Goodbye 👋")
            break

        if user_input.strip() == "":
            continue

        # detect context
        intent, mood = detect_context(user_input)

        # update state
        conversation_state["topic"] = intent

        if intent == "emotional":
            conversation_state["emotion_level"] += 1
        else:
            conversation_state["emotion_level"] = max(
                0, conversation_state["emotion_level"] - 0.2
            )

        # store input
        conversation_history.append({"user": user_input})

        # generate response
        response = generate_response(
            user_input,
            intent,
            mood,
            conversation_history,
            conversation_state
        )

        # save response
        conversation_history[-1]["nova"] = response

        # typing effect
        print("\nNOVA is typing...", end="", flush=True)
        time.sleep(random.uniform(0.8, 1.8))
        print("\rNOVA:", response, " " * 10, "\n")


if __name__ == "__main__":
    run_chat()