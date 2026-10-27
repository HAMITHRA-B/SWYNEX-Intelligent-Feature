import re
from difflib import SequenceMatcher


def normalize_text(text):
    """Convert text to lowercase and remove unnecessary punctuation."""
    if not isinstance(text, str):
        raise ValueError("Input must be a valid text string.")

    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def calculate_similarity(expected_answer, student_answer):
    """Calculate a similarity score between two answers."""

    if not isinstance(expected_answer, str) or not isinstance(student_answer, str):
        raise ValueError("Both answers must be strings.")

    expected = normalize_text(expected_answer)
    student = normalize_text(student_answer)

    if not expected:
        raise ValueError("Expected answer cannot be empty.")

    if not student:
        raise ValueError("Student answer cannot be empty.")

    # Compare the words in both answers.
    expected_words = set(expected.split())
    student_words = set(student.split())

    # Calculate word overlap.
    common_words = expected_words.intersection(student_words)
    union_words = expected_words.union(student_words)

    if union_words:
        word_overlap = len(common_words) / len(union_words)
    else:
        word_overlap = 0.0

    # Calculate sequence similarity.
    sequence_similarity = SequenceMatcher(
        None, expected, student
    ).ratio()

    # Combine both similarity measures.
    score = (0.6 * word_overlap) + (0.4 * sequence_similarity)

    return round(score * 100, 2)


def evaluate_answer(question, expected_answer, student_answer):
    """Evaluate an answer and return its score and feedback."""

    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question cannot be empty.")

    score = calculate_similarity(expected_answer, student_answer)

    if score >= 70:
        feedback = "High similarity. Your answer covers many of the expected words and patterns."
        status = "High Similarity"

    elif score >= 40:
        feedback = "Partial similarity. Review the expected answer and improve your explanation."
        status = "Partial Similarity"

    else:
        feedback = "Low similarity. Review the topic and try answering again."
        status = "Low Similarity"

    return {
        "question": question.strip(),
        "expected_answer": expected_answer.strip(),
        "student_answer": student_answer.strip(),
        "score": score,
        "status": status,
        "feedback": feedback,
    }
