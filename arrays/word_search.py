"""Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution(object):

    def __init__(self):
        self._board = None
        self._n = None
        self._m = None
        self._visited = None

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def n(self):
        if self._n is None:
            self._n = len(self._board)

        return self._n

    @property
    def m(self):
        if self._m is None:
            self._m = len(self._board[0])

        return self._m

    @property
    def visited(self):
        if self._visited is None:
            self._visited = [[0] * self.m for _ in range(self.n)]

        return self._visited

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        starting_match_ind = 0

        for i in xrange(self.n):
            for j in xrange(self.m):
                if word[0] == self.board[i][j]:
                    if self.remaining_exist(word, i, j, starting_match_ind):
                        return True
        return False

    def remaining_exist(self, word, i, j, ind):
        if len(word) == ind:
            return True

        within_range = 0 <= i < self.n and 0 <= j < self.m
        if not within_range:
            return False

        if self.board[i][j] != word[ind] or self.visited[i][j]:
            return False

        self.visited[i][j] = True
        if (self.remaining_exist(word, i - 1, j, ind + 1) or
            self.remaining_exist(word, i + 1, j, ind + 1) or
            self.remaining_exist(word, i, j - 1, ind + 1) or
            self.remaining_exist(word, i, j + 1, ind + 1)
            ):
            return True

        self.visited[i][j] = False
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist(board, 'ABCCED') == True
    assert Solution().exist(board, 'SEE') == True
    assert Solution().exist(board, 'ABCB') == False
