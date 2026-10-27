import unittest

from evaluator import calculate_similarity, evaluate_answer


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.question = "What is machine learning?"
        self.expected = (
            "Machine learning enables computers to learn patterns from data."
        )

    def test_identical_answers(self):
        score = calculate_similarity(
            self.expected,
            self.expected
        )
        self.assertEqual(score, 100.0)

    def test_score_is_within_range(self):
        score = calculate_similarity(
            self.expected,
            "Machine learning is useful."
        )
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_empty_expected_answer(self):
        with self.assertRaises(ValueError):
            calculate_similarity("", "Some answer")

    def test_empty_student_answer(self):
        with self.assertRaises(ValueError):
            calculate_similarity(self.expected, "")

    def test_empty_question(self):
        with self.assertRaises(ValueError):
            evaluate_answer("", self.expected, "Some answer")

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            calculate_similarity(None, "Some answer")

    def test_evaluation_returns_required_fields(self):
        result = evaluate_answer(
            self.question,
            self.expected,
            self.expected
        )

        self.assertIn("score", result)
        self.assertIn("status", result)
        self.assertIn("feedback", result)

    def test_identical_answer_has_high_similarity(self):
        result = evaluate_answer(
            self.question,
            self.expected,
            self.expected
        )

        self.assertEqual(result["score"], 100.0)
        self.assertEqual(result["status"], "High Similarity")


if __name__ == "__main__":
    unittest.main()
