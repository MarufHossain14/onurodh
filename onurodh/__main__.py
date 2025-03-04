import argparse
from onurodh.yeet import Yeeter  # Adjusted the import to "onurodh"


def parse_args():
    """
    Parses command-line arguments.
    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    Arguments:
        -f, --filepath (str, required): Path to the request file (.json, .yaml, or .yml format).
        -c, --colorize (bool, optional): Enable colorized output for stdout and stderr.
    """
    """Parses command-line arguments."""  
    ap = argparse.ArgumentParser(
        description="Process a request file and apply colorization if enabled.",  # Improved argparse description
        allow_abbrev=False
    )
    ap.add_argument(
        "-f", "--filepath",
        type=str,
        required=True,
        help="Path to the request file (.json, .yaml, or .yml format)",
    )
    ap.add_argument(
        "-c", "--colorize",
        action='store_true',  
        help="Enable colorized output for stdout and stderr",
    )
    
    return ap.parse_args()

def main():
    args = parse_args()
    if not args.filepath.lower().endswith(('.json', '.yaml', '.yml')):
        raise ValueError("Unsupported file format. Please provide a .json, .yaml, or .yml file.")  
    yeeter = Yeeter(colorize=args.colorize) 
    yeeter.yeet(args.filepath)

if __name__ == "__main__":
    main()
