import unittest
from challenge import remove_duplicates
# Your implementation of remove_duplicates function goes here

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_empty_list(self):
        input_list = []
        result = remove_duplicates(input_list)
        self.assertEqual(result, [])

    def test_remove_duplicates_no_duplicates(self):
        input_list = [1, 2, 3, 4, 5]
        result = remove_duplicates(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_remove_duplicates_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        result = remove_duplicates(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_remove_duplicates_mixed_data_types(self):
        input_list = [1, "apple", "orange", 2, 1, "apple"]
        result = remove_duplicates(input_list)
        self.assertEqual(result, [1, "apple", "orange", 2])

    def test_remove_duplicates_large_list(self):
        input_list = [1] * 1000 + [2] * 1000 + [3] * 1000
        result = remove_duplicates(input_list)
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

