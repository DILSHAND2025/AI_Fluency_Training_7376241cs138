from config import ask_model
from tool import search_problem_statements


questions = [
    "What is Natural Language Processing?",
    "Which hackathon problem statements are related to cybersecurity?",
    "Which cybersecurity problem statements are suitable for a team with Java, Python and web-development skills?"
]

print("=== WITH TOOL ===")

for i, question in enumerate(questions, 1):
    print(f"\nQuestion {i}: {question}")

    if i == 1:
        answer = ask_model(question)
        print("LLM Answer:")
        print(answer)

    elif i == 2:
        tool_result = search_problem_statements(domain="Cybersecurity")

        print("Tool Call:")
        print('search_problem_statements(domain="Cybersecurity")')

        final_prompt = f"""
Question: {question}

The external tool returned this information:
{tool_result}

Answer the question using the tool information. Clearly mention the matching
problem statement IDs, titles, and technologies.
"""

        answer = ask_model(final_prompt)

        print("Final Answer:")
        print(answer)

    elif i == 3:
        tool_result = search_problem_statements(domain="Cybersecurity")

        print("Tool Call:")
        print('search_problem_statements(domain="Cybersecurity")')

        final_prompt = f"""
Question: {question}

The external tool returned this information:
{tool_result}

Using only the tool information, identify which problem statements match
the team's Java, Python, and web-development skills. Explain why.
"""

        answer = ask_model(final_prompt)

        print("Final Answer:")
        print(answer)