import unittest


def selection_sort(arr):
    if not arr:
        return

    n = len(arr)
    for i in xrange(n - 1):
        min_j = i
        for j in xrange(i + 1, n):
            if arr[j] < arr[min_j]:
                min_j = j
        arr[i], arr[min_j] = arr[min_j], arr[i]


class SelectionSortTest(unittest.TestCase):
    def test_already_sorted_array_remains_sorted(self):
        inp_array = [1, 2, 3, 4, 5, 6]
        expected_array = [1, 2, 3, 4, 5, 6]

        selection_sort(inp_array)

        self.assertEquals(inp_array, expected_array)

    def test_sort_completely_unsorted_array(self):
        inp_array = [6, 5, 4, 3, 2, 1]
        expected_array = [1, 2, 3, 4, 5, 6]

        selection_sort(inp_array)

        self.assertEquals(inp_array, expected_array)

    def test_sort_partially_sorted_array_with_duplicates(self):
        inp_array = [5, 1, 3, 1, 2, 3, 6, 5]
        expected_array = [1, 1, 2, 3, 3, 5, 5, 6]

        selection_sort(inp_array)

        self.assertEquals(inp_array, expected_array)


if __name__ == '__main__':
    unittest.main()
