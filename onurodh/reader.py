import json
import yaml

def read_file(filepath: str) -> Union[dict, list]:
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
    """Reads JSON or YAML file and returns parsed content."""
    try:
        with open(filepath, 'r') as file:
            if filepath.endswith(".json"):
                return json.load(file)
            elif filepath.endswith((".yml", ".yaml")):
                return yaml.safe_load(file)
            else:
                raise ValueError("Unsupported file format. Use .json or .yaml/.yml")
    except Exception as e:
        raise RuntimeError(f"Error reading file {filepath}: {e}")