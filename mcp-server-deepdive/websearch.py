from mcp.server.fastmcp import FastMCP
from openai import OpenAI

API_KEY = '...' # Replace with your actual OpenAI API key
mcp = FastMCP("Web Search")

def web_search(query: str) -> str:
    """
    Performs a web search for your query and returns the results.
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are a web search agent. You will receive a query and you need to perform a web search to find relevant information."
            ),
        },
        {
            "role": "user",
            "content": (query),
        }
    ]

    client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="pplx-70b-chat",
        messages=messages,
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run()