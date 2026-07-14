import streamlit as st

st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 CodeMentor AI")
st.caption(
    "AI-powered feedback for DSA solutions, complexity analysis, "
    "hints, and optimization suggestions."
)

problem_statement = st.text_area(
    "Problem statement",
    height=180,
    placeholder="Paste the DSA problem here...",
)

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(
        "Programming language",
        ["Python", "Java", "C++", "JavaScript"],
    )

with col2:
    review_mode = st.selectbox(
        "Review mode",
        [
            "Beginner-friendly",
            "Hint only",
            "Interview-style",
            "Full review",
        ],
    )

code = st.text_area(
    "Your solution",
    height=320,
    placeholder="Paste your code here...",
)

if st.button("Review solution", type="primary"):
    if not problem_statement.strip():
        st.warning("Please enter the problem statement.")
    elif not code.strip():
        st.warning("Please enter your solution.")
    else:
        st.success("Your solution is ready for AI review.")
        st.write("**Selected language:**", language)
        st.write("**Review mode:**", review_mode)
        st.info("Next, we will connect this interface to the Gemini API.")