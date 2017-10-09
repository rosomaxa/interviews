"""Determine whether an integer is a palindrome.

Do this without extra space.
"""
import unittest


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None or x < 0:
            return False

        if x < 10:
            return True

        div = 1
        while x/div >= 10:
            div *= 10

        while x > 0:
            first = x % 10
            last = x / div
            if first != last:
                return False

            x = (x % div) / 10
            div = div / 100  # 10 for the first and 10 for the last digits

        return True


class NumberPalindromeTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_is_palindrome(self, n):
        self.assertTrue(self.solution.isPalindrome(n))

    def assert_is_not_palindrome(self, n):
        self.assertFalse(self.solution.isPalindrome(n))

    def test_not_palindrome_for_none(self):
        self.assert_is_not_palindrome(None)

    def test_not_palindrome_for_negative_numbers(self):
        self.assert_is_not_palindrome(-1)
        self.assert_is_not_palindrome(-10)
        self.assert_is_not_palindrome(-11)
        self.assert_is_not_palindrome(-9999)
        self.assert_is_not_palindrome(-2147447412)

    def test_not_palindrome(self):
        self.assert_is_not_palindrome(10)
        self.assert_is_not_palindrome(123421)
        self.assert_is_not_palindrome(55665)

    def test_palindrome(self):
        self.assert_is_palindrome(1)
        self.assert_is_palindrome(9)
        self.assert_is_palindrome(0)
        self.assert_is_palindrome(11)
        self.assert_is_palindrome(12321)
        self.assert_is_palindrome(543212345)
        self.assert_is_palindrome(1221)
        self.assert_is_palindrome(98766789)


if __name__ == "__main__":
    unittest.main()

