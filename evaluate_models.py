import csv
from rule_based import RuleBasedChatbot
from transformer_chatbot import TransformerChatbot

rule_bot = RuleBasedChatbot()
transformer_bot = TransformerChatbot()


def normalise_label(label: str) -> str:
    return label.strip().lower().replace("_", " ")


with open("test_queries.csv", "r", encoding="utf-8") as infile, \
     open("evaluation_results.csv", "w", newline="", encoding="utf-8-sig") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = [
        "query",
        "expected_intent",
        "rule_intent",
        "rule_confidence",
        "rule_correct",
        "transformer_intent",
        "transformer_confidence",
        "transformer_correct"
    ]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        query = row["query"]
        expected = normalise_label(row["expected_intent"])

        rule_result = rule_bot.get_response(query)
        transformer_result = transformer_bot.get_response(query)

        rule_intent = normalise_label(rule_result["intent"])
        transformer_intent = normalise_label(transformer_result["intent"])

        writer.writerow({
            "query": query,
            "expected_intent": expected,
            "rule_intent": rule_intent,
            "rule_confidence": rule_result["confidence"],
            "rule_correct": int(rule_intent == expected),
            "transformer_intent": transformer_intent,
            "transformer_confidence": transformer_result["confidence"],
            "transformer_correct": int(transformer_intent == expected)
        })

print("Evaluation complete. Results saved to evaluation_results.csv")