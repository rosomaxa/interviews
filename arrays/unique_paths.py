"""A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0] * m for _ in xrange(n)]
        for i in xrange(n):
            grid[i][0] = 1

        for j in xrange(m):
            grid[0][j] = 1

        for i in xrange(1, n):
            for j in xrange(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]


if __name__ == '__main__':
    assert Solution().uniquePaths(6, 4) == 56
