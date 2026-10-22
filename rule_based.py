import json
from pathlib import Path


class RuleBasedChatbot:
    def __init__(self, intents_path: str = "intents.json") -> None:
        path = Path(intents_path)
        with path.open("r", encoding="utf-8") as f:
            self.intents = json.load(f)

    def get_response(self, user_input: str) -> dict:
        text = user_input.lower().strip()

        best_intent = None
        best_score = 0

        for intent, data in self.intents.items():
            score = 0
            for keyword in data["keywords"]:
                if keyword in text:
                    score += 1

            if score > best_score:
                best_score = score
                best_intent = intent

        if best_intent:
            return {
                "intent": best_intent,
                "response": self.intents[best_intent]["response"],
                "confidence": 1.0 if best_score > 0 else 0.0,
                "model": "rule_based"
            }

        return {
            "intent": "fallback",
            "response": "I’m not sure I understood that. Could you rephrase your banking query?",
            "confidence": 0.0,
            "model": "rule_based"
        }