from pathlib import Path

def write_text_file(filepath: str, content: str) -> None:
    """Writes text to a file using UTF-8 encoding."""
    path = Path(filepath)
    path.write_text(content, encoding="utf-8")
    print(f"[Custom Module] Successfully wrote to {path.name}")

def read_text_file(filepath: str) -> str:
    """Reads and returns text from a file."""
    path = Path(filepath)
    if not path.exists():
        return "Error: File does not exist."
    return path.read_text(encoding="utf-8")