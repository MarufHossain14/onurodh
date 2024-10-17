class Colorizer:
    def colorize(self, text):
        # Add color codes for terminal output, e.g., green for success, red for errors
        return f"\033[92m{text}\033[0m"  # Example: wrapping in green color
