from private_data import EXPENSES


def find_transactions(category: str, month: str) -> list[dict]:
    return [
        row for row in EXPENSES
        if row["category"].lower() == category.lower() and row["date"].startswith(month)
    ]


def add_amounts(rows: list[dict]) -> float:
    return sum(row["amount"] for row in rows)


def largest_transaction(rows: list[dict]) -> dict:
    return max(rows, key=lambda row: row["amount"])