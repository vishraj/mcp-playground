from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DeploymentDeepDive")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The sum of the two integers.
    """
    return a + b
