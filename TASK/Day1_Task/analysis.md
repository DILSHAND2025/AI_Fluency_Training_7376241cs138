# Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## Scenario

I chose a small personal budgeting scenario with fictional private data. The data is a list of March expenses, including food, transport, bills, and entertainment. The user asks: **“How much did I spend on food in March, what was the largest item, and what should I review?”** The correct result from the private list is **$312.25**. The largest food transaction is **Family meal ($96.00)**.

This data is stored in `private_data.py`. It is only available to the workflow and the agent's local tools. It is not included in the plain chatbot request.

## Plain chatbot

The plain chatbot sends only the user's words to an LLM. It does not read `private_data.py`, and it has no search or calculation tool. With no API key, the program gives a safe fallback explaining that it cannot access the private expense list. With the optional Groq key, it sends the question to the model, but still does not send the private data. The model can explain how to solve the question, but it cannot know the real total unless somebody provides the data.

The chatbot is simple and flexible for normal conversation. Its limitation in this scenario is factual access. If it gives a confident number, that number is not verified against my private list. This is why a chatbot should not be used alone for a private financial answer.

## Rule-based workflow

The workflow uses no LLM. I wrote fixed Python steps: read the list, keep dates beginning with `2025-03` and category `Food`, add the matching amounts, and select the largest amount. For the chosen question it gives the same correct answer every time: $312.25 and Family meal at $96.00.

The workflow can access private data because the programmer connected it directly to the list. It is reliable for this exact request and is very fast. Its weakness is rigidity. If I ask for unusual spending, compare two months, or use a different phrase that was not considered while writing the conditions, the workflow needs new rules.

## AI agent

The agent combines an LLM, tools, and a loop. The tools are `find_transactions`, `add_amounts`, and `largest_transaction`. The agent first reasons that it needs the March Food rows, calls the search tool, and observes the matching rows. It then calls the total tool and observes $312.25. Next it calls the largest-transaction tool and observes Family meal. Since all parts of the question are answered, it stops the loop and returns the result.

The model is allowed to provide an optional final budgeting suggestion, but the private transaction rows stay inside the Python program. This is more flexible than the fixed workflow because the agent can decide which operations are needed for a new request. The disadvantages are extra complexity, possible wrong tool choices, model errors, API dependence, and the need for a maximum step limit.

## Comparison table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | Flexible language, but no private facts | Low; only programmed cases | High; can plan several operations |
| Decision-making | Generates a reply but cannot verify the list | Uses fixed `if` steps | Chooses tools and decides when finished |
| Tool usage | No tools | Direct list filtering and arithmetic | Search, total, and largest-item tools |
| Private-data access | None | Direct access in Python | Controlled access through tools |
| Multi-step task handling | Explains steps but does not perform them | Performs its one fixed sequence | Performs a reason-act-observe loop |
| Automation | Low for this question | High for known questions | High, but needs monitoring |
| Reliability | Risk of an unverified answer | High for the programmed format | Good with tools, but model decisions add risk |

## Suitability analysis

For this exact monthly expense question, the rule-based workflow is the most suitable. It is simple, fast, repeatable, and easy to check. The answer does not need open-ended reasoning because the steps are already known. A finance or student-budgeting application could use this kind of workflow for regular reports.

The AI agent is more suitable when the question changes, for example: “Find unusual spending, compare food with transport, and tell me what I should review.” That task needs several decisions and operations, so the agent can choose tools and continue after seeing results. The plain chatbot is suitable for general budgeting explanations or writing a message, but not for calculating a private total that it cannot access.

## Conclusion

A plain chatbot is best for conversation, explanations, and writing where a verified private-data lookup is not needed. A rule-based workflow is best for stable, repetitive tasks where the inputs and conditions are known and reliability is important. An AI agent is best for flexible multi-step tasks where it must interpret the request, select tools, observe results, and continue until the task is complete. The main lesson from this assessment is that an agent is not only an LLM response: it is an LLM connected to tools and a loop.