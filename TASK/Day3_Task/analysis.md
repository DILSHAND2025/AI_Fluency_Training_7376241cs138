# Agentic AI: From Prompt to Action

## 1. What is an LLM?

A Large Language Model (LLM) is an AI model trained on a large amount of text data. It can understand natural-language prompts and generate human-readable responses. An LLM is useful for tasks such as explanation, summarization, question answering, and generating text.

## 2. What is an Agent?

An agent is a system that uses an LLM to decide what action should be taken to complete a task. Instead of only generating an answer, an agent can interact with external tools when additional information or computation is required.

## 3. What is a Tool and What is a Tool Call?

A tool is an external function or service that provides information or performs an operation that the LLM cannot reliably perform by itself.

A tool call is the request made by the LLM or agent to execute that tool with specific arguments.

In this project, the tool is `search_problem_statements()`. It searches a local collection of hackathon problem statements.

## 4. What is a Tool Schema?

A tool schema describes how a tool can be used. It specifies information such as the tool name, its purpose, its input parameters, and the expected input types.

For example, the problem-statement search tool accepts:

- `domain`
- `technology`

These parameters allow the tool to filter the available problem statements.

## 5. Step-by-Step Tool Call Flow

The tool-enabled workflow in this project is:

1. The user provides a question.
2. The LLM receives the question.
3. The LLM determines whether external problem-statement information is needed.
4. The tool is called with the required parameters.
5. The tool searches the problem-statement data.
6. The tool returns the matching results.
7. The LLM uses the returned information to generate the final answer.

## 6. Why Should a Tool Return Text Even When It Fails?

A tool should return a clear text response even when no result is found or an operation fails. This allows the LLM to understand what happened and communicate it to the user instead of receiving an unclear or empty response.

For example, this tool returns:

`No matching problem statements found.`

when there are no matching results.

## 7. Plain LLM vs LLM with an External Tool

| Aspect | Plain LLM | LLM with External Tool |
|---|---|---|
| Source of information | Uses information available from the model | Uses information returned by the external tool |
| External fetch/compute | No external tool is used | Uses the problem-statement lookup tool |
| Reliability | Can provide a useful general answer, but may not know the specific local dataset | Can provide answers based on the actual data returned by the tool |
| Transparency | The source of specific information may not be visible | The tool call and returned results can be recorded |
| Speed / Cost | Usually faster because no tool execution is required | May take additional time because the tool must be executed |

In this project, the plain LLM could explain Natural Language Processing without any external information. However, for the hackathon questions, the tool-enabled version could access the specific problem-statement dataset and identify PS001 and PS004 as cybersecurity problem statements.

The comparison demonstrates that an external tool is useful when the answer depends on information that is outside the LLM's direct response context.

## 8. Experiment Observations

The first question, "What is Natural Language Processing?", could be answered directly by the LLM without using the external tool. The answer provided a general explanation of NLP and its common tasks.

For the second question, "Which hackathon problem statements are related to cybersecurity?", the plain LLM could only provide general cybersecurity examples because it did not have access to the project's specific problem-statement data. In contrast, the tool-enabled version called `search_problem_statements(domain="Cybersecurity")` and returned PS001 and PS004 from the local dataset.

For the third question, the tool-enabled version again used the external data to compare the available cybersecurity problem statements with the team's Java, Python, and web-development skills. It identified the technologies associated with PS001 and PS004 and explained the matches.

This experiment shows that an LLM can handle general knowledge questions by itself, while an external tool is useful when the answer depends on a specific dataset that is not part of the model's direct context.

## 8. Experiment Observations

The first question, "What is Natural Language Processing?", could be answered directly by the LLM without using the external tool. The answer provided a general explanation of NLP and its common tasks.

For the second question, "Which hackathon problem statements are related to cybersecurity?", the plain LLM could only provide general cybersecurity examples because it did not have access to the project's specific problem-statement data. In contrast, the tool-enabled version called `search_problem_statements(domain="Cybersecurity")` and returned PS001 and PS004 from the local dataset.

For the third question, the tool-enabled version again used the external data to compare the available cybersecurity problem statements with the team's Java, Python, and web-development skills. It identified the technologies associated with PS001 and PS004 and explained the matches.

This experiment shows that an LLM can handle general knowledge questions by itself, while an external tool is useful when the answer depends on a specific dataset that is not part of the model's direct context.