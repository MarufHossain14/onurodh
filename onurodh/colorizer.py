class Colorizer:
    COLORS = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }
    
    def colorize(self, text: str, color: str = "green") -> str:
        return f"{self.COLORS.get(color, self.COLORS['reset'])}{text}{self.COLORS['reset']}"

