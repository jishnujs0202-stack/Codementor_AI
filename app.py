import streamlit as st

from ai_reviewer import AIReviewerError, review_solution


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

with st.sidebar:
    st.header("CodeMentor AI")
    st.write("Version 1.0")
    st.divider()
    st.write("Features")
    st.write("• Correctness review")
    st.write("• Complexity analysis")
    st.write("• Bug detection")
    st.write("• Interview feedback")

problem_statement = st.text_area(
    "Problem statement",
    height=180,
    placeholder="Paste the complete DSA problem here...",
)

column_one, column_two = st.columns(2)

with column_one:
    language = st.selectbox(
        "Programming language",
        ["Python", "Java", "C++", "JavaScript"],
    )

with column_two:
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

analyze_clicked = st.button(
    "🚀 Analyze Solution",
    type="primary",
    use_container_width=True,
)

if analyze_clicked:
    if not problem_statement.strip():
        st.warning("Please enter the problem statement.")

    elif not code.strip():
        st.warning("Please enter your solution.")

    else:
        with st.spinner("CodeMentor AI is reviewing your solution..."):
            try:
                review = review_solution(
                    problem_statement=problem_statement.strip(),
                    code=code.strip(),
                    language=language,
                    review_mode=review_mode,
                )

                st.success("Review completed.")
                st.divider()
                st.subheader("AI Review")
                st.markdown(review)

            except AIReviewerError as exc:
                st.error(str(exc))