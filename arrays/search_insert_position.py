"""Given a sorted array and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""
import unittest


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)


class SearchInsertTest(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def assert_inserted_index(self, input_array, target, expected_index):
        actual_index = self.sut.searchInsert(input_array, target)
        self.assertEquals(actual_index, expected_index)

    def test_return_zero_if_empty_array(self):
        input_array = []
        target = 1
        expected_index = 0

        self.assert_inserted_index(input_array, target, expected_index)

    def test_return_zero_if_first_element_is_greater_than_target(self):
        input_array = [2, 3, 4]
        target = 1
        expected_index = 0

        self.assert_inserted_index(input_array, target, expected_index)

    def test_return_len_array_if_target_is_greater_than_last_element(self):
        input_array = [2, 3, 4]
        target = 5
        expected_index = 3

        self.assert_inserted_index(input_array, target, expected_index)

    def test_return_middle_ind_if_target_is_greater_than_first_half(self):
        input_array = [1, 3, 5, 6]
        target = 5
        expected_index = 2

        self.assert_inserted_index(input_array, target, expected_index)

    def test_return_two_if_target_is_less_than_first_element_only(self):
        input_array = [1, 3, 5, 6]
        target = 2
        expected_index = 1

        self.assert_inserted_index(input_array, target, expected_index)


if __name__ == "__main__":
    unittest.main()
