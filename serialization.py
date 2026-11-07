import csv 
import json 
import pickle 
from pathlib import Path 


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "serialization_demo"
DATA_DIR.mkdir(exist_ok=True)

json_file = DATA_DIR / "config.json"

# Python dictionary to serialize
user_settings = {
    "theme": "dark",
    "notifications": True,
    "max_connections": 100,
    "allowed_roles": ["admin", "editor"]
}

# Serialization: Python dict -> JSON file

print("[JSON] Writing data...")
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(user_settings, f, indent=4)

# deserialization: JSON file -> Python dict

print("[JSON] Reading data...")
with open(json_file, "r", encoding="utf-8") as f:
    loaded_settings = json.load(f)

print(f"  -> Loaded Theme: {loaded_settings['theme']}")
print(f"  -> Loaded Max Connections: {loaded_settings['max_connections']}\n")

