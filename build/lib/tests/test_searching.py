import unittest

from pyalgorithms.searching import binary_search


class TestSearchAlgorithm(unittest.TestCase):
    def setUp(self):
        # to test numeric numbers
        self.arr = list(range(10))

        # to test alphabets
        string = "python"
        self.alphaarr = list(string)


class TestBinarySearch(TestSearchAlgorithm):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 4), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 2), 1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertIs(binary_search.binary_search(self.arr, 9), 9)
        self.assertIs(binary_search.binary_search(self.alphaarr, 't'), 2)
        self.assertIs(binary_search.binary_search(self.arr, 't'), False)


# Test Runner
if __name__ == '__main__':
    unittest.main()
