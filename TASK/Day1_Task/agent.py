from config import ask_model
from tools import add_amounts, find_transactions, largest_transaction


REQUEST = "How much did I spend on food in March, what was the largest item, and what should I review?"


def agent() -> str:
    print("AGENT LOOP")
    print("Reason: I need March Food transactions first.")
    rows = find_transactions("Food", "2025-03")
    print(f"Act: find_transactions('Food', '2025-03') -> {len(rows)} rows")
    print("Observe: the matching private rows are available locally.")

    total = add_amounts(rows)
    print(f"Act: add_amounts(rows) -> ${total:,.2f}")
    print("Observe: the total is available.")

    largest = largest_transaction(rows)
    print(f"Act: largest_transaction(rows) -> {largest['item']}")
    print("Observe: all requested facts are available, so the loop stops.")

    model_summary = ask_model(
        f"Write one short budgeting suggestion after food spending was ${total:,.2f} "
        f"and the largest item was {largest['item']} (${largest['amount']:,.2f})."
    )
    suggestion = model_summary if model_summary and not model_summary.startswith("Model request failed") else (
        "Review whether the family meal was planned and compare it with the monthly food budget."
    )
    return (
        f"Food total: ${total:,.2f}\n"
        f"Largest item: {largest['item']} (${largest['amount']:,.2f})\n"
        f"Review: {suggestion}"
    )


if __name__ == "__main__":
    print(agent())