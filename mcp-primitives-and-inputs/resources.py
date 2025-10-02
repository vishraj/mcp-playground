from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Returns an overview of the inventory.
    """

    overview = """
    Inventory Overview:
    - Coffee
    - Tea
    - Cookies
    """

    return overview.strip()

inventory_id_to_price = {
    "123": "6.99",
    "456": "17.99",
    "789": "84.99"
}

inventory_name_to_id = {
    "Coffee": "123",
    "Tea": "456",
    "Cookies": "789"
}

@mcp.resource("inventory://{inventory_id}/price")
def get_inventory_price_from_inventory_id(inventory_id: str) -> str:
    """
    Returns the price of an inventory item given its ID.
    """

    price = inventory_id_to_price.get(inventory_id, "Unknown ID")
    return price

@mcp.resource("inventory://{inventory_name}/id")
def get_inventory_id_from_inventory_name(inventory_name: str) -> str:
    """
    Returns the ID of an inventory item given its name.
    """

    inventory_id = inventory_name_to_id.get(inventory_name, "Unknown Name")
    return inventory_id

if __name__ == "__main__":
    mcp.run()