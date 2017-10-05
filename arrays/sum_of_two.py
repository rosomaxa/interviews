"""Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Trick: array is unsorted, need to return indices without changing the order. 
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_to_ind = {val: i for i, val in enumerate(nums)}

        for i, num in enumerate(nums):
            diff = target - num
            j = val_to_ind.get(diff)
            if j and j != i:
                return i, j

        return -1


if __name__ == "__main__":
    nums = [3, 2, 0, 8]
    target = 10
    assert Solution().twoSum(nums, target) == (1, 3)
