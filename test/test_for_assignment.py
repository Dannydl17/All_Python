import unittest

from assignment import list_to_dictionary


class TestCornFlakes(unittest.TestCase):
    def test_list_to_dictionary_func(self):
        actual = list_to_dictionary.can_convert_list_to_dictionary(['apple', 'banana', 'coconut'])
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(actual, expected)

    def test_list_to_dictionary_func_to_upper(self):
        actual = list_to_dictionary.can_convert_list_to_dictionary(['apple', 'banana', 'coconut', 'corn'])
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'}
        self.assertEqual(actual, expected)
