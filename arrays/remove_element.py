"""Given an array and a value,
remove all instances of that value in place and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2,
with the first two elements of nums being 2.
"""
import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        start = 0
        end = len(nums)
        while start < end:
            if nums[start] == val:
                nums[start] = nums[end - 1]
                del nums[-1]
                end -= 1
            else:
                start += 1
        return start


class RemoveElementTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.val = 1

    def test_return_zero_for_none_array(self):
        nums = None
        actual_length = self.s.removeElement(nums, self.val)
        self.assertEquals(actual_length, 0)

    def test_return_zero_for_empty_array(self):
        nums = []
        actual_length = self.s.removeElement(nums, self.val)
        self.assertEquals(actual_length, 0)

    def test_returns_same_array_length_for_value_not_in_array(self):
        nums = [2, 3, 4]
        expected_length = 3

        actual_length = self.s.removeElement(nums, self.val)
        self.assertEquals(actual_length, expected_length)

    def test_return_zero_given_array_of_one_element_and_same_value(self):
        nums = [1]

        actual_length = self.s.removeElement(nums, self.val)
        self.assertEquals(actual_length, 0)
        self.assertEquals(nums, [])

    def test_return_zero_for_array_with_same_values_given_same_value(self):
        nums = [1, 1, 1]

        actual_length = self.s.removeElement(nums, self.val)
        self.assertEquals(actual_length, 0)
        self.assertEquals(nums, [])

    def test_return_one_time_less_if_val_has_one_occurence_in_array(self):
        nums = [2, 3, 4, 1, 5]
        expected_length = len(nums) - 1

        actual_length = self.s.removeElement(nums, self.val)
        self.assertEquals(actual_length, expected_length)
        self.assertEquals(nums, [2, 3, 4, 5])

    def test_returns_array_reduced_by_val_given_duplicates(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_length = len(nums) - 2
        expected_nums = [2, 2]

        actual_length = self.s.removeElement(nums, val)
        self.assertEquals(actual_length, expected_length)
        self.assertEquals(nums, expected_nums)


if __name__ == "__main__":
    unittest.main()
