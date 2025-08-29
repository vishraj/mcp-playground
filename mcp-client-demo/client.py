from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

# specify the server params
server_params = StdioServerParameters(
    command = "uv",
    args = ["run", "weather.py"]
)

async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                print("Listing tools")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool ...")
                result = await session.call_tool("get_weather", arguments={"location": "California"})

                print("Tool result:", result)
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(run())
    