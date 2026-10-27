# SWYNEX Intelligent Feature

An interactive Python and Streamlit application that evaluates
answers using text similarity, generates feedback, and demonstrates
input validation and automated testing.

## Features

- Similarity-based answer evaluation
- Scores from 0 to 100
- Feedback based on similarity thresholds
- Interactive Streamlit interface
- Built-in evaluation examples
- Input validation and error handling
- Automated unit tests
- Documentation of failure cases and limitations

## Technologies

- Python
- Streamlit
- unittest
- difflib

## Project Structure

- app.py: Streamlit user interface
- evaluator.py: Evaluation and scoring logic
- test_evaluator.py: Automated tests
- requirements.txt: Dependencies
- examples.md: Evaluation examples and failure cases
- README.md: Project documentation

## Installation

Install Python 3.10 or later.

Install dependencies:

pip install -r requirements.txt

## Run the Application

streamlit run app.py

## Run Tests

python -m unittest -v test_evaluator.py

## Evaluation Method

The evaluator combines word-set overlap and sequence similarity.

The resulting score measures textual similarity, not factual correctness.
The evaluation thresholds are demonstration settings and may require
adjustment based on a larger test dataset.

## Limitations

Text similarity cannot fully understand meaning or verify facts.
Future improvements could include semantic embeddings, a labeled
evaluation dataset, precision and recall measurements, and an
independent semantic evaluation model.

## Internship Task

SWYNEX Internship - Task 3: Intelligent Feature
