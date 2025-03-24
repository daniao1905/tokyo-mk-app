import json

def get_tokyo_routes():
    with open("tokyo_destinos.json", "r", encoding="utf-8") as f:
        return json.load(f)
