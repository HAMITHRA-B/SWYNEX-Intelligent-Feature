import streamlit as st
from evaluator import evaluate_answer


st.set_page_config(
    page_title="AI Study Evaluator",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Intelligent AI Study Evaluator")

st.write(
    "Evaluate an answer using text similarity, receive feedback, "
    "and explore different evaluation examples."
)

st.info(
    "This tool measures textual similarity. It does not independently "
    "verify factual correctness."
)

st.subheader("Enter Your Answer")

question = st.text_input(
    "Question",
    placeholder="What is machine learning?"
)

expected_answer = st.text_area(
    "Expected Answer",
    placeholder="Enter the answer you want to compare against."
)

student_answer = st.text_area(
    "Your Answer",
    placeholder="Enter your answer here."
)

if st.button("Evaluate Answer", type="primary"):

    if not question.strip():
        st.error("Please enter a question.")

    elif not expected_answer.strip():
        st.error("Please enter the expected answer.")

    elif not student_answer.strip():
        st.error("Please enter your answer.")

    else:
        try:
            result = evaluate_answer(
                question,
                expected_answer,
                student_answer
            )

            st.subheader("Evaluation Results")

            st.metric(
                label="Text Similarity Score",
                value=f"{result['score']:.2f}%"
            )

            st.progress(
                min(max(result["score"] / 100, 0.0), 1.0)
            )

            st.write("**Evaluation Status:**", result["status"])
            st.write("**Feedback:**", result["feedback"])

        except ValueError as error:
            st.error(f"Input error: {error}")

        except Exception as error:
            st.error(
                "An unexpected error occurred. "
                "Please check your inputs and try again."
            )

st.divider()

st.subheader("🧪 Try Evaluation Examples")

examples = {
    "High Similarity": (
        "Machine learning enables computers to learn patterns from data.",
        "Machine learning allows computers to learn patterns from data."
    ),
    "Partial Similarity": (
        "Machine learning enables computers to learn patterns from data.",
        "Machine learning is a field of artificial intelligence."
    ),
    "Low Similarity": (
        "Machine learning enables computers to learn patterns from data.",
        "The Earth revolves around the Sun."
    )
}

selected_example = st.selectbox(
    "Choose an example",
    list(examples.keys())
)

if st.button("Run Example"):

    expected, student = examples[selected_example]

    try:
        result = evaluate_answer(
            "What is machine learning?",
            expected,
            student
        )

        st.write("**Expected Answer:**", expected)
        st.write("**Sample Answer:**", student)

        st.metric(
            "Similarity Score",
            f"{result['score']:.2f}%"
        )

        st.write("**Status:**", result["status"])
        st.write("**Feedback:**", result["feedback"])

    except ValueError as error:
        st.error(str(error))
