def compute_match_score(resume_text: str, jd_keywords: list):
    resume_lower = (resume_text or "").lower()
    matched, missing = [], []

    for kw in jd_keywords:
        if kw in resume_lower:
            matched.append(kw)
        else:
            missing.append(kw)

    if not jd_keywords:
        return {"score": None, "matched": [], "missing": []}

    score = round(len(matched) / len(jd_keywords) * 100, 1)
    return {"score": score, "matched": matched, "missing": missing}
