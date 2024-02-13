import unittest
from task1 import first_occurrence


class TestFirstOccurrence(unittest.TestCase):
    def test_biggest_odd(self):
        first_string = 'restart'
        self.assertEqual(first_occurrence.first_occurrence(first_string),'resta$t')
