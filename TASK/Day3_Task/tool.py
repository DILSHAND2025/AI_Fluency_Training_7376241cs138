PROBLEM_STATEMENTS = [
    {
        "id": "PS001",
        "domain": "Cybersecurity",
        "technologies": ["Python", "NLP", "Machine Learning"],
        "title": "AI-Based Phishing Email Detection",
    },
    {
        "id": "PS002",
        "domain": "Healthcare",
        "technologies": ["Python", "Machine Learning"],
        "title": "Early Disease Risk Prediction System",
    },
    {
        "id": "PS003",
        "domain": "Agriculture",
        "technologies": ["Python", "Computer Vision"],
        "title": "Crop Disease Detection",
    },
    {
        "id": "PS004",
        "domain": "Cybersecurity",
        "technologies": ["Java", "NLP", "Web Development"],
        "title": "Automated Threat Intelligence Platform",
    },
    {
        "id": "PS005",
        "domain": "Education",
        "technologies": ["Java", "Web Development"],
        "title": "Smart Student Learning Platform",
    },
]


def search_problem_statements(
    domain=None,
    technology=None,
):
    results = []

    for problem in PROBLEM_STATEMENTS:
        domain_match = (
            domain is None
            or domain.lower() in problem["domain"].lower()
        )

        technology_match = (
            technology is None
            or any(
                technology.lower() in tech.lower()
                for tech in problem["technologies"]
            )
        )

        if domain_match and technology_match:
            results.append(problem)

    if not results:
        return "No matching problem statements found."

    return results


if __name__ == "__main__":
    print(search_problem_statements(domain="Cybersecurity"))