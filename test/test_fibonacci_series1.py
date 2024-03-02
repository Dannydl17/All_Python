import unittest
from assignment import fibonacci_series1


class Test(unittest.TestCase):
    def test_can_return_fibonacci_number(self):
        number = 6
        result = [0, 1, 1, 2, 3, 5]
        self.assertEqual(result, fibonacci_series1.can_return_fibonacci_number(number))

    def test_that_the_highest_fibonacci_number_can_be_the_largest_number_test(self):
        result = [0,1,1,2,3,5]
        number = 5
        self.assertEqual(number, fibonacci_series1.can_find_the_largest_number(result))