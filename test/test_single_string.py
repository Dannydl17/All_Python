import unittest
from exercises_class import two_characters


class TestTwoCharactersExercise(unittest.TestCase):
    def test_two_character(self):
        words = 'abc,xyz'
        results = two_characters.can_pick_single_string(words)
        self.assertEqual('xyc abz', results)
