# Evaluation Examples and Failure Cases

## Project

SWYNEX Intelligent AI Study Evaluator

## Evaluation Method

The application combines word-set overlap and sequence similarity
to calculate a text similarity score from 0 to 100.

The score is an approximate similarity measure. It does not prove
that an answer is factually correct.

## Example 1: Identical Answer

Expected answer:
Machine learning enables computers to learn patterns from data.

Submitted answer:
Machine learning enables computers to learn patterns from data.

Expected result:
- Similarity score: 100%
- Status: High Similarity

## Example 2: Similar Answer

Expected answer:
Machine learning enables computers to learn patterns from data.

Submitted answer:
Machine learning allows computers to learn patterns from data.

Expected result:
- High textual similarity
- Status should be determined by the implemented scoring thresholds.

## Example 3: Different Answer

Expected answer:
Machine learning enables computers to learn patterns from data.

Submitted answer:
The Earth revolves around the Sun.

Expected result:
- Low textual similarity
- Status should be determined by the implemented scoring thresholds.

## Failure Cases

1. Empty question:
   The application asks the user to enter a question.

2. Empty expected answer:
   The application asks the user to enter an expected answer.

3. Empty submitted answer:
   The application asks the user to enter an answer.

4. Invalid evaluation input:
   The evaluator raises a ValueError for invalid text types.

## Limitations

- Similarity does not guarantee factual correctness.
- Different wording can reduce the similarity score.
- Incorrect answers containing similar words may receive higher scores.
- The thresholds are simple demonstration settings and require further evaluation.

## Testing

Run the automated tests with:

python -m unittest -v test_evaluator.py

Record the actual test results before submitting the project.
