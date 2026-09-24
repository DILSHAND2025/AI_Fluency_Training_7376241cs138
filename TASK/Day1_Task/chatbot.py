from config import ask_model


REQUEST = "How much did I spend on food in March, what was the largest item, and what should I review?"


def chatbot(request: str = REQUEST) -> str:
    # The private list is intentionally not passed to the model.
    response = ask_model(request)
    if response:
        return response
    return (
        "I do not have access to your private expense list, so I cannot calculate the total. "
        "You would need to filter March food transactions and add them yourself."
    )


if __name__ == "__main__":
    print("PLAIN CHATBOT")
    print("Request:", REQUEST)
    print("Answer:", chatbot())