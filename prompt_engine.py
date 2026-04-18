import random

"""
Response engine for NOVA assistant.

Generates context-aware replies based on:
- user intent
- emotional state
- conversation history
- response variation
"""


# small human-like fillers
micro_replies = [
    "hmm…",
    "yeah…",
    "I see…",
    "okay…",
    "right…"
]

# emotional reflection phrases
reflections = [
    "that sounds tough…",
    "I can imagine that’s not easy…",
    "hmm… that must feel heavy…"
]


def generate_response(user_input, intent, mood, history, state):
    """
    Generate a response based on context and emotional continuity.

    Args:
        user_input (str): current user message
        intent (str): detected intent (emotional/study/productivity/casual)
        mood (str): detected mood
        history (list): previous conversation messages
        state (dict): tracks emotion level and topic

    Returns:
        str: generated response
    """

    # get previous user input (for memory reference)
    last_user = history[-2]["user"] if len(history) > 1 else None

    # randomly decide whether to reference past context
    use_memory = random.choice([True, False])

    # -------- EMOTIONAL RESPONSES --------
    if intent == "emotional":

        level = state["emotion_level"]

        if level == 1:
            responses = [
                "Hey… I'm here. Want to talk about what's going on?",
                "That sounds a bit heavy… what's been bothering you?"
            ]

        elif level == 2:
            responses = [
                "It sounds like this has been building up… when did it start?",
                "You've been feeling this for a while… want to talk more about it?"
            ]

        elif level >= 3:
            responses = [
                "That kind of feeling can get really exhausting over time… what do you think is causing it?",
                "When something stays this long, there's usually more underneath… want to explore that?"
            ]

        else:
            responses = [
                "I'm here with you. What's going on?",
                "You can tell me anything… I'm listening."
            ]

        # optional memory reference
        if use_memory and last_user:
            responses.append("Is this connected to something you mentioned earlier?")

        # persistence awareness
        if level >= 2:
            responses.append("You've been feeling this for a bit now… want to open up more?")

    # -------- STUDY RESPONSES --------
    elif intent == "study":

        # if user is emotionally affected
        if state["emotion_level"] >= 0.5:
            responses = [
                "I get it… feeling low and having an exam isn’t easy. let’s take it step by step—what topic are you on?",
                "That’s tough timing… your mind’s already heavy. let’s just focus on one small thing."
            ]
        else:
            responses = [
                "Let's break it down step by step. What part is confusing?",
                "We'll figure it out together. Where exactly are you stuck?",
                "Try explaining what you understand so far — I'll help fill the gaps."
            ]

        if use_memory and last_user:
            responses.append("Are you still working on the same topic as before?")

    # -------- PRODUCTIVITY RESPONSES --------
    elif intent == "productivity":

        if state["emotion_level"] >= 0.5:
            responses = [
                "Makes sense you can’t focus… when your mind feels heavy, it’s hard. let’s start with one small step.",
                "I get why focusing feels tough right now… don’t push too hard. just try something simple."
            ]
        else:
            responses = [
                "Let's start small. What's one thing you can do right now?",
                "Focus on just one task. What's your next step?",
                "Don't overthink — start and adjust as you go."
            ]

        if use_memory and last_user:
            responses.append("Still trying to get back on track from earlier?")

    # -------- CASUAL RESPONSES --------
    else:
        responses = [
            "Hmm… I'm listening. Go on.",
            "Alright… what's on your mind?",
            "That's interesting. Tell me more.",
            "I'm here — what do you feel like talking about?"
        ]

        if use_memory and last_user:
            responses.append("You were saying something earlier… want to continue that?")

    # -------- PICK RESPONSE --------
    base_response = random.choice(responses)

    # add emotional reflection occasionally
    if intent == "emotional" and random.random() < 0.5:
        base_response = f"{random.choice(reflections)} {base_response}"

    # avoid repeated filler words
    for word in ["yeah…", "hmm…"]:
        base_response = base_response.replace(f"{word} {word}", word)

    # add small human-like prefix occasionally
    if random.random() < 0.4:
        prefix = random.choice(micro_replies)
        return f"{prefix} {base_response}"

    return base_response