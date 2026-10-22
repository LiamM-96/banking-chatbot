from flask import Flask, render_template, request, jsonify
from rule_based import RuleBasedChatbot
from transformer_chatbot import TransformerChatbot
from logger_util import initialise_log, log_interaction

app = Flask(__name__)

rule_bot = RuleBasedChatbot()
transformer_bot = TransformerChatbot()
initialise_log()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    selected_model = data.get("model", "rule_based")

    if selected_model == "rule_based":
        result = rule_bot.get_response(user_message)
    elif selected_model == "transformer":
        result = transformer_bot.get_response(user_message)
    else:
        result = {
            "intent": "fallback",
            "response": "Invalid chatbot model selected.",
            "confidence": 0.0,
            "model": "unknown"
        }

    log_interaction(user_message, result)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)