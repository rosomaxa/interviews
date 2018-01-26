"""Given a list of non negative integers,
arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large,
so you need to return a string instead of an integer.
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if len(nums) == 1:
            return str(nums[0])

        new_sorted = map(str, nums)

        new_sorted.sort(
            cmp=lambda a, b: 0 if a == b else
            1 if b + a > a + b else
            -1 if a + b > b + a else
            0
        )
        if new_sorted[0] == '0':
            return '0'

        return ''.join(new_sorted)


if __name__ == '__main__':
    print Solution().largestNumber([920, 9, 2, 1])
    print Solution().largestNumber([0, 0, 0])

    print Solution().largestNumber([9, 5, 0, 1])
    print Solution().largestNumber([29, 5, 0, 1])
    print Solution().largestNumber([3, 30, 34, 5, 9])
