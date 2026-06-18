import os
import json


def sanitize(name):
    invalid = '<>:"/\\|?*'
    for char in invalid:
        name = name.replace(char, "_")
    return name


def load_progress():
    if not os.path.exists("progress.json"):
        return {"completed": []}

    try:
        with open("progress.json", "r", encoding="utf-8") as f:
            content = f.read().strip()

            if not content:
                return {"completed": []}

            return json.loads(content)

    except:
        return {"completed": []}


def save_progress(progress):
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=4)