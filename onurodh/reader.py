import json
import yaml

def read_file(filepath):
    """
    Reads the content of a file and returns it as a Python object.

    The function supports JSON and YAML file formats. It raises a ValueError
    if the file format is not supported.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        dict or list: The content of the file as a Python object.

    Raises:
        ValueError: If the file format is not supported.

    Examples:
        >>> read_file('data.json')
        {'key': 'value'}

        >>> read_file('config.yaml')
        {'key': 'value'}
    """
    if filepath.endswith(".json"):
        with open(filepath, 'r') as file:
            return json.load(file)
    elif filepath.endswith(".yml") or filepath.endswith(".yaml"):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError("Unsupported file format. Use .json or .yaml/.yml")
