import os
import sys

# Get the project root folder:
# AI fluency traning assessment
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Paths to required folders
DAY1_DIR = os.path.join(ROOT_DIR, "LAB", "Day1_TRANING")
DAY2_TASK_DIR = os.path.join(ROOT_DIR, "TASK", "Day2_Task")

# Add required folders to Python path
for path in (ROOT_DIR, DAY1_DIR, DAY2_TASK_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)

from config import ask_model
from inventory_tools import inventory_snapshot, reorder_quantity, stock_status


QUESTION = (
    "I need to know which inventory items are at or below their reorder point, "
    "how many units of the low-stock items need to be ordered, and what is the total stock across all SKUs?"
)


def agent(question: str, max_steps: int = 8) -> str:
    print("AGENT LOOP")
    print(f"Question: {question}\n")

    snapshot = inventory_snapshot()

    print(
        "Thought: I need the inventory table first so I can identify "
        "low-stock items and compute the reorder quantities."
    )

    print(f"Action: inventory_snapshot() -> {len(snapshot)} SKUs")

    print("Observation: the stock table is available locally.")

    low_items = []
    total_stock = 0
    reorder_total = 0

    for item in snapshot:
        total_stock += item["stock"]

        status = stock_status(item)

        if status in {"reorder", "low"}:
            low_items.append(item)
            reorder_total += reorder_quantity(item)

    print(
        "Thought: I have the stock data and am checking which SKUs "
        "are at or below their reorder levels."
    )

    print(
        f"Action: stock_status() and reorder_quantity() on each SKU "
        f"-> {len(low_items)} items flagged"
    )

    print(
        "Observation: the low-stock set is known and the ordered "
        "quantities can be calculated."
    )

    recommendation = (
        "Review the low-stock items and place orders for the SKUs "
        "that are at or below their reorder points."
    )

    if not low_items:
        recommendation = (
            "No item is currently below the reorder threshold; "
            "inventory looks healthy."
        )

    answer = (
        f"Total stock across all SKUs: {total_stock}\n"
        f"Low-stock / reorder items: "
        f"{', '.join(item['sku'] for item in low_items) if low_items else 'None'}\n"
        f"Reorder quantity needed: {reorder_total}\n"
        f"Recommendation: {recommendation}"
    )

    return answer


if __name__ == "__main__":
    print(agent(QUESTION, max_steps=8))