import unittest
from Class_work import triple_list


class TestListExercise(unittest.TestCase):
    def test_triple_list(self):
        num = [3, 7, 2, 6, 5]
        result = [27, 343, 8, 216, 125]
        self.assertEqual(result, triple_list.triple_list(num))
