import csv
from pathlib import Path
from datetime import datetime


LOG_FILE = Path("chat_logs.csv")


def initialise_log() -> None:
    if not LOG_FILE.exists():
        with LOG_FILE.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "user_message",
                "intent",
                "response",
                "confidence",
                "model"
            ])


def log_interaction(user_message: str, result: dict) -> None:
    with LOG_FILE.open("a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            user_message,
            result.get("intent", ""),
            result.get("response", ""),
            result.get("confidence", 0.0),
            result.get("model", "")
        ])