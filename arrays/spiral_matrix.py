"""Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def left_to_right(self, r_markers, c_markers):
        pairs = [(r_markers[0], ind) for ind in c_markers]
        del r_markers[0]
        return pairs

    def right_to_left(self, r_markers, c_markers):
        pairs = [(r_markers[-1], ind) for ind in reversed(c_markers)]
        del r_markers[-1]
        return pairs

    def top_down(self, r_markers, c_markers):
        pairs = [(ind, c_markers[-1]) for ind in r_markers]
        del c_markers[-1]
        return pairs

    def bottom_up(self, r_markers, c_markers):
        pairs = [(ind, c_markers[0]) for ind in reversed(r_markers)]
        del c_markers[0]
        return pairs

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        rows_num = len(matrix)
        cols_num = len(matrix[0])

        r_markers = [i for i in xrange(rows_num)]
        c_markers = [i for i in xrange(cols_num)]

        result = []
        spiral_sequence = [self.left_to_right, self.top_down,
                           self.right_to_left, self.bottom_up]
        step_num = 0
        while r_markers and c_markers:
            step = spiral_sequence[step_num % len(spiral_sequence)]

            this_sublist = step(r_markers, c_markers)
            result.extend(matrix[x][y] for x, y in this_sublist)
            step_num += 1

        return result

if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print Solution().spiralOrder(m)
