import unittest


def all_sum(data):
    result = ''
    for i in data:
        result += str(i)
    return result


class TestAllSum(unittest.TestCase):

    def test_mixed_numbers(self):
        mixed_numbers = [1, 2.5, 3]
        result_numbers = '12.53'
        self.assertEqual(all_sum(mixed_numbers), result_numbers)

    def test_mixed_numbers_strings(self):
        mixed_numbers_strings = [1, 'cat', 2.5]
        result_numbers_strings = '1cat2.5'
        self.assertEqual(all_sum(mixed_numbers_strings), result_numbers_strings)

    def test_empty(self):
        empty = []
        result_empty = ''
        self.assertEqual(all_sum(empty), result_empty)


if __name__ == '__main__':
    unittest.main()