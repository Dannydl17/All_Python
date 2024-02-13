import unittest
from task1 import equal_strings


class TestListExercise(unittest.TestCase):
    def test_biggest_odd(self):
        first_string = ('loveer')
        second_string = ('evol')
        self.assertFalse(equal_strings.can_return_equal_string(first_string, second_string))
