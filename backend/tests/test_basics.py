import unittest

from app import create_app
from app.models import Level
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

    def test_build_level_list(self):
        game_levels = Level.get_all()
        formatted_levels = [level.assemble() for level in game_levels]
        self.assertTrue(formatted_levels)
        print(formatted_levels)
