"""Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
return 2 because 13 = 4 + 9.
"""


import math


class Solution(object):
    def get_perfect_squares_for(self, n):
        result = []
        start = 1
        while start ** 2 <= n:
            result.append(start ** 2)
            start += 1
        return result

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = self.get_perfect_squares_for(n)
        root = [[n]]
        count = 0
        while root:
            count += 1
            this_level = root.pop()
            next_level = []
            for num in this_level:
                for sq in squares:
                    if num == sq:
                        return count
                    if num < sq:
                        break

                    next_level.append(num - sq)

            if next_level:
                root.append(next_level)

        return count


if __name__ == '__main__':
    print Solution().numSquares(2)
    print Solution().numSquares(4)
    print Solution().numSquares(13)
    print Solution().numSquares(12)
