import re

COMMON_SKILLS = [
    "python", "sql", "excel", "tableau", "power bi", "r",
    "pandas", "numpy", "statistics", "machine learning",
    "data visualization", "eda", "a/b testing",
    "dashboards", "reporting", "data cleaning"
]

def extract_jd_keywords(job_description: str):
    text = (job_description or "").lower()
    found = set()

    for skill in COMMON_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found.add(skill)

    return sorted(found)
