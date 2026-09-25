from config import ask_model


questions = [
    "What is Natural Language Processing?",
    "Which hackathon problem statements are related to cybersecurity?",
    "Which cybersecurity problem statements are suitable for a team with Java, Python and web-development skills?"
]

print("=== WITHOUT TOOL ===")

for i, question in enumerate(questions, 1):
    print(f"\nQuestion {i}: {question}")

    answer = ask_model(question)

    print("LLM Answer:")
    print(answer)