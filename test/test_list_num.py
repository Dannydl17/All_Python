import unittest
from Class_work import list_class


class TestListNum(unittest.TestCase):
    def test_list_class_return_list_from_1_to_20(self):
        result = list(range(1, 21))
        self.assertEqual(list_class.list_number(), result)

    def test_list_class_return_odd_numbers(self):
        list1 = list(range(1, 21))
        result = list(range(1, 21, 2))
        self.assertEqual(list_class.list_number2(list1), result)

    def test_list_class_double_odd_numbers(self):
        list1 = list(range(1, 21))
        result = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
        self.assertEqual(list_class.list_number3(list1), result)

    def test_list_class_change_some_numbers_to_zero(self):
        list1 = list(range(1, 21))
        result = [2, 6, 10, 14, 0, 0, 0, 0, 34, 38]
        self.assertEqual(list_class.list_number4(list1), result)

    def test_function_can_concatenate_two_list(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        list3 = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(list_class.list_number5(list1, list2), list3)
