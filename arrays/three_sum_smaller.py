"""Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy
the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
"""
import unittest


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        count = 0
        nums.sort()

        for i in xrange(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                this_sum = nums[i] + nums[j] + nums[k]
                if this_sum < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count


class ThreeSumSmallerTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_returns_zero_given_empty_nums(self):
        expected_count = 0

        actual_count = self.s.threeSumSmaller([], 2)

        self.assertEquals(expected_count, actual_count)

    def test_find_correct_triplet_count_for_valid_case(self):
        self.assertEquals(1, self.s.threeSumSmaller([-2, 0, 1], 2))
        self.assertEquals(2, self.s.threeSumSmaller([-2, 0, 1, 3], 2))
        self.assertEquals(
            34, self.s.threeSumSmaller([-2, 0, 1, 3, 1, -4, 0], 5))


if __name__ == "__main__":
    unittest.main()
