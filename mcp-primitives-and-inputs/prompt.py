from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Prompt")

@mcp.prompt()
def get_prompt(topic: str) -> str:
    """
    Returns a prompt that will do a detailed analysis on a given topic.
    Args:
        topic (str): The topic to analyze.
    """
    return f"Do a detailed analysis on this topic: {topic}."

if __name__ == "__main__":
    mcp.run()