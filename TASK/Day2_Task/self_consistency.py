import os
import re
import sys
from collections import Counter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DAY1_DIR = os.path.join(ROOT_DIR, "LAB", "Day1_TRANING")
for path in (ROOT_DIR, DAY1_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)

from config import MODEL, client


QUESTION = (
    "A warehouse has five SKUs with stock counts 9, 14, 6, 18, and 11. "
    "What is the total stock across all SKUs, and what is the average stock per SKU? "
    "Reason step by step and end with exactly: Final Answer: <answer>."
)


def ask_once(question: str, temperature: float = 0.8) -> str:
    if client is None:
        return "No API key configured."
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a careful warehouse analyst."},
            {"role": "user", "content": question},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def extract_final_answer(text: str) -> str:
    match = re.search(r"Final Answer:\s*(.+)", text, flags=re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return "No final answer found"


if __name__ == "__main__":
    answers = []
    print("Self-consistency check (5 CoT runs at temperature=0.8)\n")
    for i in range(5):
        raw = ask_once(QUESTION, temperature=0.8)
        answer = extract_final_answer(raw)
        answers.append(answer)
        print(f"Run {i + 1}: {answer}")
    counts = Counter(answers)
    print("\nMajority answer:", counts.most_common(1)[0][0])
    print("Counts:", dict(counts))
