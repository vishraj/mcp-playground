from mcp.server.fastmcp import FastMCP
from pathlib import Path

NOTES_FILE = Path(__file__).resolve().with_name("notes.txt")

mcp = FastMCP("LocalNotes")

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to a local .txt file.
    Args:
        content (str): The content to append to the file.
    """

    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        return f"Content appended to {NOTES_FILE}"
    except Exception as e:
        return f"Error appending to file {NOTES_FILE}: {e}"

@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the content of the local notes.txt file.
    """

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.read()
        return notes if notes else "The notes file is empty."
    except FileNotFoundError:
        return f"Error: The file {NOTES_FILE} does not exist."
    except Exception as e:
        return f"Error reading file {NOTES_FILE}: {e}"


if __name__ == "__main__":
    mcp.run()