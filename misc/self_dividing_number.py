"""A self-dividing number is a number that is divisible by
every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in xrange(left, right + 1):
            dividers = self.get_dividers(i)
            if dividers and all(i % div == 0 for div in dividers):
                result.append(i)

        return result

    def get_dividers(self, i):
        number = i
        dividers = []
        while number > 0:
            number, y = divmod(number, 10)
            if y == 0:
                return []

            dividers.append(y)
        return dividers


if __name__ == '__main__':
    assert Solution().selfDividingNumbers(
        1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
