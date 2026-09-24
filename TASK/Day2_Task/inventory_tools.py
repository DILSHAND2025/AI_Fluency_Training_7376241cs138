INVENTORY = {
    "SKU-101": {
        "name": "USB-C Hub",
        "stock": 18,
        "reorder_point": 10,
        "target_level": 25,
        "supplier": "Northline Tech",
    },
    "SKU-202": {
        "name": "Wireless Mouse",
        "stock": 6,
        "reorder_point": 12,
        "target_level": 22,
        "supplier": "Northline Tech",
    },
    "SKU-303": {
        "name": "4K Monitor",
        "stock": 14,
        "reorder_point": 8,
        "target_level": 20,
        "supplier": "DisplayWorks",
    },
    "SKU-404": {
        "name": "Mechanical Keyboard",
        "stock": 9,
        "reorder_point": 11,
        "target_level": 21,
        "supplier": "KeyCraft",
    },
    "SKU-505": {
        "name": "Laptop Stand",
        "stock": 23,
        "reorder_point": 15,
        "target_level": 28,
        "supplier": "DeskFlow",
    },
}


def find_inventory(sku: str) -> dict | None:
    key = sku.strip().upper()
    item = INVENTORY.get(key)
    if item is None:
        return None
    return {**item, "sku": key}


def inventory_snapshot() -> list[dict]:
    return [
        {"sku": sku, **item}
        for sku, item in INVENTORY.items()
    ]


def stock_status(item: dict) -> str:
    stock = item["stock"]
    reorder_point = item["reorder_point"]
    if stock <= reorder_point:
        return "reorder"
    if stock <= reorder_point + 4:
        return "low"
    return "healthy"


def reorder_quantity(item: dict) -> int:
    return max(0, item["target_level"] - item["stock"])
