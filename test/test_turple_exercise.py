import unittest
from list_file import turple1


class TestListExercise(unittest.TestCase):
    def test_that_tuple_list_can_be_reverse(self):
        nums = (10, 20, 30, 40, 50)
        result = (50, 40, 30, 20, 10)
        self.assertEqual(result, turple1.reverse_tuple(nums))
