from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import pyautogui
import io


# create server
mcp = FastMCP("ScreenshotTool")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Captures a screenshot of the current screen and returns it as an Image object.
    """
    
    buffer = io.BytesIO()


    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format='JPEG', quality=60, optimize=True)
    return Image(data=buffer.getvalue(), format="jpeg")


if __name__ == "__main__":
    mcp.run()
    

