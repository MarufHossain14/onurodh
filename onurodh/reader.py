import json
import yaml

def read_file(filepath):
    if filepath.endswith(".json"):
        with open(filepath, 'r') as file:
            return json.load(file)
    elif filepath.endswith(".yml") or filepath.endswith(".yaml"):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError("Unsupported file format. Use .json or .yaml/.yml")
