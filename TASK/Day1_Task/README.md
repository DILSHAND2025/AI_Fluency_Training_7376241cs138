# Day 1 Assessment: Three Ways to Answer a Private-Data Question

I chose a small student budgeting example. The private data is a fictional list of my March expenses. The question is: **How much did I spend on food in March, what was the largest item, and what should I review?**

Run it with the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run_all.py
```

To run each assessment system separately for screenshots:

```powershell
python chatbot.py
python workflow.py
python agent.py
```

The project works offline using the local fallback. To try the optional Groq response, copy `.env.example` to `.env` and add a newly rotated key. Never commit `.env`.

