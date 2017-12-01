import unittest


def merge_sort(S):
    n = len(S)
    if n < 2:
        return

    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S, S1, S2)


def merge(S, S1, S2):
    i = 0
    j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


class MergeSortTest(unittest.TestCase):
    def test_already_sorted_array_remains_sorted(self):
        inp_array = [1, 2, 3, 4, 5, 6]
        expected_array = [1, 2, 3, 4, 5, 6]

        merge_sort(inp_array)

        self.assertEquals(inp_array, expected_array)

    def test_sort_completely_unsorted_array(self):
        inp_array = [6, 5, 4, 3, 2, 1]
        expected_array = [1, 2, 3, 4, 5, 6]

        merge_sort(inp_array)

        self.assertEquals(inp_array, expected_array)

    def test_sort_partially_sorted_array_with_duplicates(self):
        inp_array = [5, 1, 3, 1, 2, 3, 6, 5]
        expected_array = [1, 1, 2, 3, 3, 5, 5, 6]

        merge_sort(inp_array)

        self.assertEquals(inp_array, expected_array)


if __name__ == '__main__':
    unittest.main()
