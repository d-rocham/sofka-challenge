import unittest

from app import create_app
from app.models import Level, Questions
from flask import current_app


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])


class CreateQuestionCase(BasicTestCase):
    """Test exceptions in Questions.create_question() method"""

    # Define wrong arguments
    short_questions = {"foo": "bar"}
    long_questions = {"foo": "bar", "faz": "foo", "bar": "foo"}

    wrong_questions_keys = [
        {"foo": "bar", "level_id": 4},
        {"question_text": "text", "foo": "bar"},
    ]

    inexistent_level = {"question_text": "PREGUNTA DE PRUEBA", "level_id": 7}

    short_answers = {"foo": "bar"}
    long_answers = {
        "foo_1": "bar",
        "foo_2": "bar",
        "foo_3": "bar",
        "foo_4": "bar",
        "foo_5": "bar",
    }

    no_correct_answer = {"foo_1": 0, "foo_2": 0, "foo_3": 0, "foo_4": 0}
    excessive_correct_answers = {"foo_1": 1, "foo_2": 0, "foo_3": 1, "foo_4": 0}

    # Define correct arguments:
    correct_questions = {"question_text": "PREGUNTA DE PRUEBA", "level_id": 1}
    correct_answers = {
        "answer_1": 1,
        "answer_2": 0,
        "answer_3": 0,
        "answer_4": 0,
    }

    # Tests
    def test_short_questions(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.short_questions,
            self.correct_answers,
        )

    def test_long_questions(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.long_questions,
            self.correct_answers,
        )

    def test_wrong_question_keys_text(self):
        self.assertRaises(
            KeyError,
            Questions.create_question,
            self.wrong_questions_keys[0],
            self.correct_answers,
        )

    def test_wrong_question_keys_id(self):
        self.assertRaises(
            KeyError,
            Questions.create_question,
            self.wrong_questions_keys[1],
            self.correct_answers,
        )

    def test_inexistent_level(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.inexistent_level,
            self.correct_answers,
        )

    def test_short_answers(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.correct_questions,
            self.short_answers,
        )

    def test_long_answers(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.correct_questions,
            self.long_answers,
        )

    def test_no_correct_answer(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.correct_questions,
            self.no_correct_answer,
        )

    def test_excessive_correct_answers(self):
        self.assertRaises(
            ValueError,
            Questions.create_question,
            self.correct_questions,
            self.excessive_correct_answers,
        )
