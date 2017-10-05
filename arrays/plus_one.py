"""Given a non-negative integer represented as a non-empty array of digits,
plus one to the integer.

You may assume the integer do not contain any leading zero,
except the number 0 itself.

The digits are stored such that the most significant digit is at the
head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        i = len(digits) - 1
        while i >= 0:
            this_sum = digits[i] + carry
            if i == len(digits) - 1:
                this_sum += 1
            carry, rem = divmod(this_sum, 10)
            digits[i] = rem
            i -= 1
        if carry:
            digits.insert(0, carry)
        return digits


if __name__ == "__main__":
    digits = [9, 9, 9]
    assert Solution().plusOne(digits) == [1, 0, 0, 0]

    digits = [1, 3, 9]
    assert Solution().plusOne(digits) == [1, 4, 0]

    digits = [1, 2, 3]
    assert Solution().plusOne(digits) == [1, 2, 4]