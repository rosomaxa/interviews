import unittest


def quick_sort(S):
    def _in_place_quick_sort(S, a, b):
        if a >= b:
            return

        pivot = S[b]
        left = a
        right = b - 1
        while left <= right:
            while left <= right and S[left] < pivot:
                left += 1
            while left <= right and pivot < S[right]:
                right -= 1
            if left <= right:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        S[left], S[b] = S[b], S[left]
        _in_place_quick_sort(S, a, left - 1)
        _in_place_quick_sort(S, left + 1, b)

    _in_place_quick_sort(S, 0, len(S) - 1)


class QuickSortTest(unittest.TestCase):
    def test_already_sorted_array_remains_sorted(self):
        inp_array = [1, 2, 3, 4, 5, 6]
        expected_array = [1, 2, 3, 4, 5, 6]

        quick_sort(inp_array)

        self.assertEquals(inp_array, expected_array)

    def test_sort_completely_unsorted_array(self):
        inp_array = [6, 5, 4, 3, 2, 1]
        expected_array = [1, 2, 3, 4, 5, 6]

        quick_sort(inp_array)

        self.assertEquals(inp_array, expected_array)

    def test_sort_partially_sorted_array_with_duplicates(self):
        inp_array = [5, 1, 3, 1, 2, 3, 6, 5]
        expected_array = [1, 1, 2, 3, 3, 5, 5, 6]

        quick_sort(inp_array)

        self.assertEquals(inp_array, expected_array)


if __name__ == '__main__':
    unittest.main()
