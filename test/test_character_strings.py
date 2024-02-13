import unittest
from assignment import character_string


class TestCharacterExercise(unittest.TestCase):

    def test_characterString(self):
        words = "semicolon.africa"
        result = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(character_string.count_string_and_return_dictionary(words), result)