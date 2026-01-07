Resume–Job Description Reviewer

A simple web app that compares a resume against a job description and highlights alignment gaps.
Built to help students and early-career applicants understand what they’re missing and how to improve, not to automate hiring decisions.

Live demo: (Streamlit Community Cloud link here)

What it does

You upload (or paste) a resume and optionally paste a job description.

The app returns:

A skill match summary showing which JD requirements are present or missing

A written review highlighting strengths, weaknesses, and concrete improvement suggestions

The two views are meant to complement each other: one is explicit and transparent, the other focuses on clarity and presentation.

How to use (for users)

Upload a resume (PDF, DOCX, or TXT) or paste resume text

(Optional) Enter a target role

(Optional) Paste a job description

Click Analyze Resume

Results appear in two sections:

Rule-Based JD Match: skill coverage and missing areas

Written Review: overall feedback and recommendations

No account or setup is required to use the app.

Intended scope

The skill-matching logic is designed for data, analytics, and early-career technical roles, where job descriptions clearly list tools and requirements (e.g. Python, SQL, dashboards).

For roles that are primarily narrative or credential-based (e.g. law, medicine, humanities), the written review remains useful, while the skill match should be interpreted cautiously.

Why this approach

Keyword matching alone is easy to explain but rigid.
Written feedback alone is flexible but subjective.

This project keeps both:

Explicit matching to show concrete gaps

Qualitative feedback to explain context and presentation issues

Seeing them together makes resume improvements easier to act on.

Tech overview

Python

Streamlit

OpenAI API

PDF/DOCX text extraction

Secrets are managed via environment variables and are not committed to the repository.

Running locally (optional)
pip install -r requirements.txt
streamlit run app.py


Create a .env file with:

OPENAI_API_KEY=your_api_key_here

Notes

This is a small, scoped project built for learning and practical use.
It’s intentionally focused on clarity, explainability, and responsible use rather than feature breadth.
