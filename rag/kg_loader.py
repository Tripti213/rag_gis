import json

def load_kgraph(path="kgraph.json"):
    with open(path, "r") as f:
        return json.load(f)