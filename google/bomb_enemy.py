"""Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
(the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted
point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""


class Solution(object):
    def get_enemies_vertically(self, grid, i, j, direction):
        count = 0
        while 0 <= i < len(grid) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            if direction == 'D':
                i -= 1
            else:
                i += 1
        return count

    def get_enemies_horizontally(self, grid, i, j, direction):
        count = 0
        row = grid[i]
        while 0 <= j < len(row) and row[j] != 'W':
            if row[j] == 'E':
                count += 1
            if direction == 'R':
                j += 1
            else:
                j -= 1
        return count

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        max_ = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] in ['W', 'E']:
                    continue
                enemies_here = (
                    self.get_enemies_horizontally(grid, i, j, 'L') +
                    self.get_enemies_horizontally(grid, i, j, 'R') +
                    self.get_enemies_vertically(grid, i, j, 'D') +
                    self.get_enemies_vertically(grid, i, j, 'U')
                )
                max_ = max(max_, enemies_here)
        return max_


if __name__ == '__main__':
    grid = [['0', 'E', '0', '0'],
            ['E', '0', 'W', 'E'],
            ['0', 'E', '0', '0']]

    s = Solution()
    print s.maxKilledEnemies(grid)

