import os
import sys

from collections import Counter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DAY1_DIR = os.path.join(ROOT_DIR, "DAY1")
for path in (ROOT_DIR, DAY1_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)

from config import MODEL, client


DIRECT_PROMPT = (
    "Answer only with the final answer. Do not explain your steps. "
    "Return the final answer as a short sentence or number."
)

COT_PROMPT = (
    "Reason step by step, think clearly, and then end with exactly: "
    "Final Answer: <answer>."
)


def ask(system_prompt: str, question: str) -> str:
    if client is None:
        return "No API key configured."
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


REASONING_QUESTIONS = [
    "A warehouse has 12 laptops, 7 monitors, and 3 more laptops are shipped in. How many devices are there in total?",
    "A product list has stock counts of 9, 14, 5, and 11. What is the median stock value?",
    "Three orders are for 4, 6, and 10 units. If 3 units are returned from the second order, what is the total remaining units?",
    "Sort these stock counts from lowest to highest: 18, 5, 9, 15, 7. What is the middle value after sorting?",
    "A shelf has 24 pens. If 6 are sold, then 4 more are restocked, and 5 are damaged, how many usable pens remain?",
]


if __name__ == "__main__":
    print("Direct Prompting vs Chain-of-Thought on reasoning-only questions\n")
    for idx, question in enumerate(REASONING_QUESTIONS, start=1):
        print(f"Question {idx}: {question}")
        direct_answer = ask(DIRECT_PROMPT, question)
        cot_answer = ask(COT_PROMPT, question)
        print("DIRECT:", direct_answer)
        print("COT:", cot_answer)
        print("-" * 80)
