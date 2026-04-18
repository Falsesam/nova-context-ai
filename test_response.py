from prompt_engine import generate_response

def test_response():
    history = [{"user": "i feel sad"}]
    state = {"emotion_level": 1}

    response = generate_response(
        "i feel sad",
        "emotional",
        "sad",
        history,
        state
    )

    print("Test Response:", response)


if __name__ == "__main__":
    test_response()