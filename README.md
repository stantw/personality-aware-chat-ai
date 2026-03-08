# Personality-Aware Conversational AI (MBTI)
A prototype conversational AI system that infers MBTI personality traits from natural dialogue and adapts its communication style accordingly.

This project explores whether Large Language Models (LLMs) can infer personality signals through multi-turn conversations, instead of relying on traditional questionnaire-based personality tests.

#Quick Start Overview

  Below is a quick overview of how the system works.
  <img width="554" height="1400" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/78f58144-72b6-4ace-91f5-2ce00d0871db" />
  
  The system transitions from natural conversation collection to personality inference, and finally to adaptive 
  dialogue behavior.

#Project Overview

Traditional MBTI assessments rely on static questionnaires and lack conversational context.
This project investigates whether LLMs can:
  
    × infer personality traits from natural dialogue
    × estimate MBTI personality dimensions
    × dynamically adjust conversational style
    
  The goal is not to replace psychological assessments but to explore personality-aware conversational AI systems.
  
  #System Architecture
  
    User Input
       ↓
    Conversation State Manager
       ↓
    Exploration Chat (LLM)
       ↓
    Trigger Condition Reached
       ↓
    MBTI Inference Module
       ↓
    Structured Personality Result
       ↓
    Adaptive Response Generator
       ↓
    Personality-Aware AI Reply

#Conversation Flow

- Phase 1 — Exploration

  The system begins with a natural conversation phase designed to collect behavioral and linguistic signals.
  
  To preserve conversational authenticity, the system follows a double-blind design principle:
  
      × The user does not know that personality inference is being performed.
      × The AI does not explicitly reference personality testing during dialogue.
      × This prevents the conversation from becoming questionnaire-like and helps preserve natural language behavior.
  
  Characteristics of this phase:
  
      × open-ended questions
      × conversational tone
      × contextual follow-up questions
      
  no explicit personality testing prompts

- Phase 2 — Personality Inference
  
  Once sufficient conversational data is collected (typically after ~10 dialogue turns), the system performs MBTI inference.
  The LLM analyzes the conversation and outputs structured personality predictions.
  
  Example output:
  
      {
       "E_I": "I",
       "S_N": "N",
       "T_F": "T",
       "J_P": "J",
       "MBTI": "INTJ",
       "confidence": 0.72,
       "reasoning_summary": "User shows preference for structured planning and logical reasoning."
      }
  
  Confidence Threshold
  
  If the inference confidence score is below 0.55, the system activates a fallback mechanism:
  
      * The MBTI prediction is considered unreliable
      * The conversation returns to neutral response mode
  
  This prevents unstable personality predictions from degrading the user experience.

- Phase 3 — Adaptive Chat
  
  Once a personality profile is inferred, the system adjusts its communication style accordingly.
  
      Dimension	        |     Adjustment Strategy
      Introversion (I)	|     concise replies, calm tone, fewer follow-up questions
      Extraversion (E)	|     interactive responses, extended dialogue
      Thinking (T)	    |     structured reasoning, logical explanations
      Feeling (F)         |  	  empathetic tone, emotional awareness
  
  These adjustments are intentionally lightweight in the MVP stage and mainly influence tone and conversational structure.

#Tech Stack

    - Backend
      × Python
      × FastAPI
    - LLM
      * Google Gemini API
    - Data Processing
      * Numpy
    - Frontend (MVP)
      × HTML
      × CSS
      × JavaScript

#Project Structure

    personality-aware-chat-ai/
    │
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    │
    ├── app/
    │   ├── main.py
    │   ├── config.py
    │   ├── prompts.py
    │   ├── schemas.py
    │   ├── mbti_rules.py
    │   ├── state_manager.py
    │
    │   ├── services/
    │   │   ├── llm_service.py
    │   │   ├── conversation_service.py
    │   │   ├── inference_service.py
    │   │   └── response_style_service.py
    │
    │   ├── routes/
    │   │   ├── chat.py
    │   │   └── inference.py
    │
    ├── data/
    │   ├── mbti_ground_truth.csv
    │   └── results.csv
    │
    ├── frontend/
    │   ├── index.html
    │   ├── style.css
    │   └── app.js
    │
    └── notebooks/
        └── evaluation.ipynb

#Evaluation Method

  This MVP includes a small proof-of-concept evaluation.
  Participants: 20 users
  Each participant:
  
    * completes an MBTI test first
    * engages in an AI conversation (8–12 turns)
    * system predicts MBTI traits
    
  Evaluation metric: Accuracy = correct_predictions / total_samples
  Dimensions evaluated: E/I, S/N, T/F, J/P

#Future Improvements

  Planned features for future versions:
  
    * conversation embeddings
    * vector database (FAISS / Chroma)
    * long-term personality memory
    * adaptive dialogue memory
    * personality evolution tracking
  
  Personality Score Convergence
  
  Future versions will implement personality score convergence, where personality estimates gradually stabilize 
  across multiple conversations.
  This will be achieved through time-series weighted updates, allowing personality estimates to evolve as more 
  behavioral data is observed.
  
  Example approach:
  
    * maintain running personality scores
    * apply weighted updates based on recent conversations
    * gradually converge toward a stable personality profile
  
  This allows the system to move from single-session personality inference toward long-term behavioral modeling.

#License

  MIT License
