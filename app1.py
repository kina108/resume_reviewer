import streamlit as st
from resume_parser import process_file
from jd_analysis import extract_jd_keywords
from scorer import compute_match_score
from llm_reviewer import review_with_llm

st.title("AI Resume Reviewer")
st.write("Upload your resume and optionally a job description.")

uploaded_file = st.file_uploader("Upload resume", type=["pdf", "docx", "txt"])

resume_text_input = st.text_area("Or paste resume text", height=250)
target_role = st.text_input("Target role (optional)")
job_description = st.text_area("Job description (optional)", height=200)

if st.button("Analyze Resume"):
    if uploaded_file:
        resume_text, error = process_file(uploaded_file)
        if error:
            st.error(error)
            st.stop()
    elif resume_text_input.strip():
        resume_text = resume_text_input
    else:
        st.warning("Upload a file or paste resume text.")
        st.stop()

    jd_keywords = extract_jd_keywords(job_description)
    rule_score = compute_match_score(resume_text, jd_keywords)

    if len(jd_keywords) < 3:
        st.info(
            "Rule-based matching is optimized for data and analytics roles. "
            "For this role, rely primarily on the LLM-based review."
        )

    st.subheader("Rule-Based JD Match")
    if rule_score["score"] is None:
        st.write("No JD provided.")
    else:
        st.write(f"**Match Score:** {rule_score['score']}%")
        st.write("**Matched Keywords:**")
        st.markdown(", ".join(rule_score["matched"]) or "None")

        st.write("**Missing Keywords:**")
        st.markdown(", ".join(rule_score["missing"]) or "None")

    st.subheader("LLM-Based Review")
    with st.spinner("Analyzing..."):
        st.markdown(review_with_llm(resume_text, target_role, job_description))
