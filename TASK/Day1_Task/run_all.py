from pathlib import Path

from agent import agent
from chatbot import REQUEST, chatbot
from terminal_image import create_terminal_image
from workflow import workflow


def save(name: str, text: str) -> None:
    output = Path(__file__).parent / "Output"
    output.mkdir(exist_ok=True)
    (output / f"{name}_output.txt").write_text(text, encoding="utf-8")
    create_terminal_image(name, text)


def main() -> None:
    chatbot_result = f"Request: {REQUEST}\n\n{chatbot()}"
    workflow_result = workflow()
    agent_result = agent()
    save("chatbot", chatbot_result)
    save("workflow", workflow_result)
    save("agent", agent_result)
    print("Assessment text outputs and terminal-style PNG images saved in Output/")


if __name__ == "__main__":
    main()