import argparse
from onurodh.yeet import Yeeter  # Adjusted the import to "onurodh"

def main():
    args = parse_args()
    if not args.filepath.lower().endswith(('.json', '.yaml', '.yml')):

    yeeter.yeet(args.filepath)  # Executes the request from the given filepath

def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=True,
        help="Request filepath in .json or .yaml or .yml format",
    )
    ap.add_argument(
        "-c",
        "--colorize",
        action='store_true',
        help="Colorize stdout and stderr"
    )
    return ap.parse_args()

if __name__ == "__main__":
    main()
