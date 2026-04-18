import streamlit as st
from context_detector import detect_context
from prompt_engine import generate_response

st.title("NOVA - Context-Aware AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

if "state" not in st.session_state:
    st.session_state.state = {"emotion_level": 0}

user_input = st.text_input("You:")

if user_input:
    intent, mood = detect_context(user_input)

    if intent == "emotional":
        st.session_state.state["emotion_level"] += 1
    else:
        st.session_state.state["emotion_level"] = max(
            0, st.session_state.state["emotion_level"] - 1
        )

    st.session_state.history.append({"user": user_input})

    response = generate_response(
        user_input,
        intent,
        mood,
        st.session_state.history,
        st.session_state.state
    )

    st.session_state.history[-1]["nova"] = response

for chat in st.session_state.history:
    st.write("You:", chat["user"])
    st.write("NOVA:", chat["nova"])