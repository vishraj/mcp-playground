from mcp.server.fastmcp import FastMCP
from pathlib import Path
import requests

mcp = FastMCP("CryptoTool")

@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Gets the price of a cyrptocurrency
    
    Args:
        crypto: symbol of the cryptocurrency (e.g., BTC, ETH)
    """

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": crypto.lower(), "vs_currencies": "usd"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")
        if price is not None:
            return f"The current price of {crypto} is ${price}"
        else:
            return f"Unable to retrieve the price for {crypto}."
    except Exception as e:
        return f"Error fetching price for {crypto}: {e}"

if __name__ == "__main__":
    mcp.run()