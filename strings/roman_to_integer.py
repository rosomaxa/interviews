"""
I, II, III, IV, V, VI, VII, VIII, IX, X
XI
"""
import unittest


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if not s:
            return
        result = 0
        prev = 0
        for num in reversed(s):
            curr = roman[num]
            if prev > curr:
                result -= curr
            else:
                result += curr
            prev = curr
        return result


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.func = Solution().romanToInt

    def test_return_on_empty_str(self):
        self.assertIsNone(self.func(''))

    def test_converts_single_roman_digit(self):
        int_ = self.func('I')
        self.assertEquals(int_, 1)

        int_ = self.func('II')
        self.assertEquals(int_, 2)

        int_ = self.func('III')
        self.assertEquals(int_, 3)

        int_ = self.func('IV')
        self.assertEquals(int_, 4)

        int_ = self.func('V')
        self.assertEquals(int_, 5)

        int_ = self.func('VI')
        self.assertEquals(int_, 6)

        int_ = self.func('IX')
        self.assertEquals(int_, 9)

        int_ = self.func('X')
        self.assertEquals(int_, 10)

    def test_can_convert_multi_digit_roman(self):
        int_ = self.func('XII')
        self.assertEquals(int_, 12)

        int_ = self.func('XXXIV')
        self.assertEquals(int_, 34)

        int_ = self.func('XC')
        self.assertEquals(int_, 90)


if __name__ == '__main__':
    unittest.main()
