# NOVA – Context-Aware AI Assistant

## Overview
NOVA is a context-aware conversational assistant built to simulate more natural and human-like interactions. The system focuses on understanding not just what the user says, but also the context and emotional flow across multiple messages.

Instead of treating each input independently, NOVA maintains a short-term memory and adapts its responses based on how the conversation evolves.

---

## Problem
Most basic chatbot systems respond to inputs in isolation. This often results in:
- Repetitive responses
- Sudden topic shifts
- Lack of emotional understanding

Such interactions feel mechanical and disconnected from how real conversations work.

---

## Solution
This project attempts to address the above limitations by designing a system that:
- Identifies user intent (emotional, study, productivity, casual)
- Tracks emotional intensity over time
- Maintains conversation history
- Generates responses that adapt to both context and tone

---

## Key Features

### Context Detection
The system classifies user input into different categories based on keywords and patterns.

### Emotional Tracking
An `emotion_level` variable is used to:
- Capture ongoing emotional states
- Influence how future responses are generated
- Gradually fade instead of resetting instantly

### Conversation Memory
Recent user inputs are stored and occasionally referenced to maintain continuity without making it obvious or repetitive.

### Adaptive Responses
Responses are generated dynamically based on:
- Current intent
- Emotional state
- Previous interaction

### Context Bridging
The system avoids abrupt transitions. For example, if a user expresses stress and then mentions an exam, the assistant connects both instead of switching topics directly.

---

## Example Interaction

User: i feel sad  
NOVA: that sounds tough… I'm here. Want to talk about what's going on?

User: i have exam tomorrow  
NOVA: that’s tough timing… feeling low and having an exam isn’t easy. let’s take it step by step—what topic are you on?

User: i cant focus  
NOVA: makes sense you can’t focus… when your mind feels heavy, it’s really hard. let’s just try one small step.

---

## System Design

The project is divided into three main parts:

- **Context Detector** – identifies intent and mood  
- **State Manager** – tracks conversation flow and emotional level  
- **Response Engine** – generates adaptive replies  

---

## Tech Stack
- Python  
- Rule-based NLP techniques  
- Stateful conversation logic  

---

## Approach
The focus of this project is on **conversation design and behavior modeling** rather than using external AI APIs.

The system demonstrates how:
- Context can be tracked across multiple turns  
- Emotional continuity can be simulated  
- Responses can be adapted without relying on large models  

The architecture can be extended later using APIs such as:
- Google Gemini  
- OpenAI GPT  
- Groq / OpenRouter  

---

## Limitations
- Does not use deep learning models  
- Limited understanding compared to full-scale AI systems  
- Only supports short-term memory  

---

## Future Scope
- Integration with real-time AI APIs  
- Long-term memory system  
- Voice-based interaction  
- UI/UX improvements  

---

## Conclusion
**NOVA** -  demonstrates that even without external AI models, it is possible to design a system that simulates context-aware and emotionally adaptive conversation.

The project emphasizes the importance of conversational design, state management, and human-centric interaction in AI systems.

---

## How to Run
(in Terminal):
```bash
python main.py