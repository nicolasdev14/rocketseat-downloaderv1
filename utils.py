import os
import re
import json


def sanitize(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def load_progress():
    if not os.path.exists("progress.json"):
        return {"completed": []}

    with open("progress.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(progress):
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)