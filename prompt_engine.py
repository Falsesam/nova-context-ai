import random

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
    "I can imagine that's not easy…",
    "hmm… that must feel heavy…"
]

def generate_response(user_input, intent, mood, history, state):

    last_user = history[-2]["user"] if len(history) > 1 else None
    use_memory = random.choice([True, False])

    # -------- EMOTIONAL --------
    if intent == "emotional":

        level = state["emotion_level"]

        if level == 1:
            responses = [
                "Hey… I'm here. Want to talk about what's going on?",
                "That sounds a bit heavy… what's been bothering you?"
            ]

        elif level == 2:
            responses = [
                "Hmm… it sounds like this isn't just a one-time thing. Has it been building up?",
                "You've been feeling this for a bit now… when did it start?"
            ]

        elif level >= 3:
            responses = [
                "That kind of feeling can get really exhausting over time… what do you think is causing it deep down?",
                "When something lingers like this, there's usually more underneath… want to explore that together?"
            ]

        else:
            responses = [
                "I'm here with you. What's going on?",
                "You can tell me anything… I'm listening."
            ]

        if use_memory and last_user:
            responses.append("Is this connected to something you mentioned earlier?")

        if state["emotion_level"] >= 2:
            responses.append("Hey… you've been feeling this way for a bit now. Want to talk more about it?")

    # -------- STUDY --------
    elif intent == "study":

        if state["emotion_level"] >= 0.5:
            responses = [
                "I get it… feeling low and having an exam at the same time isn't easy. let's take it step by step—what topic are you on?",
    "That’s tough timing… your mind's already heavy. let's just pick one small thing to go over."
            ]
        else:
            responses = [
                "Let's break it down step by step. What part is confusing?",
                "We'll figure it out together. Where exactly are you stuck?",
                "Try explaining what you understand so far — I'll help fill the gaps."
            ]

        if use_memory and last_user:
            responses.append("Are you still working on the same topic as before?")

    # -------- PRODUCTIVITY --------
    elif intent == "productivity":

        if state["emotion_level"] >= 0.5:
            responses = [
                "Makes sense you can’t focus… when your mind feels heavy, it’s really hard. let’s just try one small step, okay?",
    "I get why focusing feels tough right now… don’t force it. just start with something really simple."
            ]
        else:
            responses = [
                "Let's start small. What's one thing you can do right now?",
                "Focus on just one task. What's your next step?",
                "Don't overthink — start and adjust as you go."
            ]

        if use_memory and last_user:
            responses.append("Still trying to get back on track from earlier?")

    # -------- CASUAL --------
    else:
        responses = [
            "Hmm… I'm listening. Go on.",
            "Alright… what's on your mind?",
            "That's interesting. Tell me more.",
            "I'm here — what do you feel like talking about?"
        ]

        if use_memory and last_user:
            responses.append("You were saying something earlier… want to continue that?")

    # pick one response
    base_response = random.choice(responses)

    # add emotional reflection sometimes
    if intent == "emotional" and random.random() < 0.5:
        base_response = f"{random.choice(reflections)} {base_response}"

    # add small human prefix sometimes
    if random.random() < 0.4:
        prefix = random.choice(micro_replies)
        return f"{prefix} {base_response}"

    # simple cleanup to avoid repeated filler words
    for w in ["yeah…", "hmm…"]:
        base_response = base_response.replace(f"{w} {w}", w)

    return base_response