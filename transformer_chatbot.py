from transformers import pipeline


class TransformerChatbot:
    def __init__(self) -> None:
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )

        self.labels = [
            "lost card",
            "check balance",
            "open savings account",
            "transaction query"
        ]

        self.responses = {
            "lost card": "I’m sorry to hear that. You should freeze your card immediately from the banking app or contact support.",
            "check balance": "Your current balance is shown on the account overview page in this prototype.",
            "open savings account": "You can open a savings account online through the products section of the banking app.",
            "transaction query": "Please check your recent transactions. In a full system, merchant details would be shown here."
        }

    def get_response(self, user_input: str) -> dict:
        result = self.classifier(user_input, self.labels)

        top_label = result["labels"][0]
        top_score = float(result["scores"][0])

        if top_score < 0.85:
            return {
                "intent": "fallback",
                "response": "I’m not fully confident about that request. Could you rephrase it?",
                "confidence": top_score,
                "model": "transformer"
            }

        return {
            "intent": top_label,
            "response": self.responses[top_label],
            "confidence": top_score,
            "model": "transformer"
        }