import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found. Put it in a .env file.")

URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

def review_with_llm(resume_text: str, target_role: str = "", job_description: str = "") -> str:
    role_text = (
        f"The resume is targeted for the role: {target_role}."
        if target_role else
        "Use general professional standards."
    )

    jd_text = (
        f"Here is the job description:\n{job_description}\n"
        if job_description else
        "No job description was provided."
    )

    prompt = f"""
You are an expert resume reviewer.

{role_text}
{jd_text}

Return these sections:

### Score (0-100)
### Summary
### Strengths
### Weaknesses
### Recommendations
### JD Match (0-100)

Resume:
{resume_text}
""".strip()

    payload = {
        "model": "gpt-5.1",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    r = requests.post(URL, headers=HEADERS, json=payload, timeout=60)
    if r.status_code != 200:
        return f"API Error ({r.status_code}): {r.text}"

    return r.json()["choices"][0]["message"]["content"]
