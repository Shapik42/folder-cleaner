import json
from pathlib import Path

DEFAULT_RULES: dict[str, list[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Audio_Video": [".mp3", ".wav", ".mp4", ".mkv", ".avi"],
}

def load_rules(filepath: str = "rules.json") -> dict[str, list[str]]:
    path = Path(filepath)
    if not path.exists():
        save_rules(DEFAULT_RULES, filepath)
        return DEFAULT_RULES
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_rules(rules: dict[str, list[str]], filepath: str = "rules.json") -> None:
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(rules, file, ensure_ascii=False, indent=2)
