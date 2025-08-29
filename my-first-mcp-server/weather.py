from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.

    Args:
        location (str): The location to get the weather for.

    Returns:
        str: A string describing the current weather.
    """
    # In a real implementation, you would call a weather API here.
    # For demonstration purposes, we'll return a mock response.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


if __name__ == "__main__":
    mcp.run()