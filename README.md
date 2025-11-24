# Customer Intent Detection Agent

A clean, beginner-friendly Python project that demonstrates how to build a simple AI agent system that understands user messages, detects intent, assigns urgency, and generates helpful replies — all without using machine learning. This project is ideal for learning how rule-based conversational agents work and serves as a foundation for later ML upgrades.

## Key Features

- Simple rule-based intent classification (no ML required)
- Intents supported: `refund`, `cancellation`, `billing`, `general_help`, `general`
- Urgency assigned per intent:
  - `refund` → high
  - `cancellation` → high
  - `billing` → medium
  - `general_help` → low
  - `general` → low
- Generates human-friendly replies for each intent
- Conversation memory that stores the last 20 interactions
- Easy to read, modify, and extend

## Project Architecture

The system is split into clear, small components:

- User Input → IntentAgent → ReplyAgent → Memory → Coordinator (main engine)

ASCII diagram:
```
┌────────────────────────┐
│        User Input      │
└─────────────┬──────────┘
              │
              ▼
┌────────────────────────┐
│     IntentAgent        │
│  (classifies intent)   │
└─────────────┬──────────┘
              │
              ▼
┌────────────────────────┐
│     ReplyAgent         │
│ (generates response)   │
└─────────────┬──────────┘
              │
              ▼
┌────────────────────────┐
│       Memory           │
│ (stores conversation)  │
└─────────────┬──────────┘
              │
              ▼
┌────────────────────────┐
│      Coordinator       │
│      (main engine)     │
└─────────────────────────┘
```

## Project Structure
```
CUSTOMER-AGENT-INTENT/
│
├── app.py               # Main executable script
├── requirements.txt     # Dependencies (if needed)
├── README.md            # Documentation (this file)
└── .gitignore           # Python cache + venv ignore
```

## How It Works (Brief)

- Memory: keeps the last 20 messages in a simple list.
- IntentAgent: checks user message for keywords and maps to an intent and urgency using simple rules.
- ReplyAgent: creates a friendly response based on the detected intent.
- Coordinator: saves user messages, calls IntentAgent, produces reply, stores the reply in memory, and returns the full response object.

Keyword mapping:
- "refund" → refund (high)
- "cancel" → cancellation (high)
- "invoice" / "bill" → billing (medium)
- "help" → general_help (low)
- otherwise → general (low)

## Installation

1. Clone the repo:
   git clone <repo-url>

2. Create a virtual environment:
   python -m venv .venv

3. Activate it:

- Windows (PowerShell):
  .venv\Scripts\Activate.ps1

- macOS / Linux:
  source .venv/bin/activate

4. Install dependencies (if the project adds any):
   pip install -r requirements.txt

Note: The core example is pure Python and may not require external packages.

## Run the Project

Run the main script:
```
python app.py
```

You should see interactive example output where the agent detects intents and responds automatically.

## Example Outputs

USER: I want to cancel my subscription.
```
{
  "intent": "cancellation",
  "urgency": "high",
  "reply": "I can help you cancel your subscription. Kindly provide your registered email."
}
```
--------------------------------------------------
USER: My invoice amount is wrong.
```
{
  "intent": "billing",
  "urgency": "medium",
  "reply": "It seems you have a billing concern. Please send your invoice number for verification."
}
```

## Extending the Project

Ideas for improvements:
- Add more intents and refine keyword matching (phrase matching, synonyms)
- Replace rule-based classification with a lightweight ML model
- Add sentiment detection to influence urgency or reply tone
- Build a Flask / FastAPI backend and a web UI (React)
- Persist conversations to a database
- Support multi-language responses

## Contributing

Contributions are welcome! Suggested workflow:
- Fork the repository
- Create a feature branch
- Add tests or examples if helpful
- Open a pull request describing the change

## License

This project is free to use, modify, and improve. Include the license of your choice (e.g., MIT) in your repository.

## Acknowledgements

Inspired by the logic used in customer support chatbots and simple rule-based assistants. Good for beginners, students, and prototypes.
