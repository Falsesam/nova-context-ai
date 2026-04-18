"""
Main entry point for NOVA assistant.

This file handles:
- user interaction loop
- context detection (intent + mood)
- conversation state tracking
- response generation
"""

import time
import random
from context_detector import detect_context
from prompt_engine import generate_response


print("Hi, I'm NOVA - the Context-Aware AI Assistant 🤖")
print("Type 'end' to end the chat ❤️\n")


# stores full conversation
conversation_history = []

# tracks ongoing state
conversation_state = {
    "topic": None,
    "emotion_level": 0
}


while True:
    # take user input
    user_input = input("You: ")

    # exit condition
    if user_input.lower() == "end":
        print("Goodbye 👋")
        break

    # ignore empty input
    if user_input.strip() == "":
        continue

    # -------- STEP 1: Detect context --------
    intent, mood = detect_context(user_input)

    # -------- STEP 2: Update state --------
    conversation_state["topic"] = intent

    # track emotional intensity over time
    if intent == "emotional":
        conversation_state["emotion_level"] += 1
    else:
        # slowly decay emotion instead of resetting
        conversation_state["emotion_level"] = max(
            0,
            conversation_state["emotion_level"] - 0.2
        )

    # -------- STEP 3: Store user input --------
    conversation_history.append({"user": user_input})

    # -------- STEP 4: Generate response --------
    response = generate_response(
        user_input,
        intent,
        mood,
        conversation_history,
        conversation_state
    )

    # save response into history
    conversation_history[-1]["nova"] = response

    # -------- STEP 5: Simulate typing --------
    print("\nNOVA is typing...", end="", flush=True)
    time.sleep(random.uniform(0.8, 1.8))

    print("\rNOVA:", response, " " * 10, "\n")