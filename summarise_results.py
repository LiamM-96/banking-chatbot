import csv

rule_total = 0
rule_correct = 0
transformer_total = 0
transformer_correct = 0

with open("evaluation_results.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rule_total += 1
        transformer_total += 1
        rule_correct += int(row["rule_correct"])
        transformer_correct += int(row["transformer_correct"])

rule_accuracy = rule_correct / rule_total if rule_total else 0
transformer_accuracy = transformer_correct / transformer_total if transformer_total else 0

print(f"Rule-based accuracy: {rule_accuracy:.2%} ({rule_correct}/{rule_total})")
print(f"Transformer accuracy: {transformer_accuracy:.2%} ({transformer_correct}/{transformer_total})")