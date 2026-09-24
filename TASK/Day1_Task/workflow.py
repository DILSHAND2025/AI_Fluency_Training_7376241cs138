from private_data import EXPENSES


def workflow() -> str:
    food = [
        row for row in EXPENSES
        if row["category"] == "Food" and row["date"].startswith("2025-03")
    ]
    total = sum(row["amount"] for row in food)
    largest = max(food, key=lambda row: row["amount"])
    return (
        "RULE-BASED WORKFLOW\n"
        "1. Read the private list.\n"
        "2. Keep March rows in the Food category.\n"
        "3. Add the amounts and find the largest amount.\n\n"
        f"Food total: ${total:,.2f}\n"
        f"Largest item: {largest['item']} (${largest['amount']:,.2f})\n"
        "Review: check whether the family meal was planned and within budget."
    )


if __name__ == "__main__":
    print(workflow())