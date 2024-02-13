import unittest
from task1 import biggest_odd


class TestListExercise(unittest.TestCase):
    def test_biggest_odd(self):
        num = '23569'
        self.assertEqual(biggest_odd.can_return_largest(num), 9)
