# game/utils.py
import json
from pathlib import Path

def load_quests():
    """Loads the quests from the JSON data file."""
    script_dir = Path(__file__).parent.parent
    quests_path = script_dir / 'data' / 'quests.json'
    with open(quests_path) as f:
        return json.load(f)
