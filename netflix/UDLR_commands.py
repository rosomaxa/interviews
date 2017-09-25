"""Translate input string into sequence of movements through on screen keyboard.

Possible movements:
 -up
 -down
 -left
 -right
 
alpha = ABCDEF
        GHIJKL
        MNOPQR
        STUVWX
        YZ----

"""
COLUMNS = 6
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Solution(object):
    def __init__(self):
        self._grid = None
        self._start = None
        self._columns = None
        self._rows = None
        self._letters_map = None

    @property
    def grid(self):
        if self._grid is None:
            result = []
            start, end = 0, 0
            while end <= len(ALPHA):
                end = start + COLUMNS
                this_row = ALPHA[start:end]
                result.append(this_row)
                start = end
            self._grid = result

            last_column = self._grid[-1]
            if len(last_column) < COLUMNS:
                filler = ['-'] * (COLUMNS - len(last_column))
                self._grid[-1] = last_column + ''.join(filler)

        return self._grid

    @property
    def start(self):
        if self._start is None:
            self.grid
            self._start = (0, 0)
        return self._start

    @property
    def columns(self):
        if self._columns is None:
            self._columns = len(self.grid[0])
        return self._columns

    @property
    def rows(self):
        if self._rows is None:
            self._rows = len(self.grid)

        return self._rows

    @property
    def letters_map(self):
        if self._letters_map is None:
            self._letters_map = {}
            for i, row in enumerate(self.grid):
                for j, letter in enumerate(row):
                    self._letters_map[letter] = (i, j)

        return self._letters_map

    def to_commands(self, name):
        result = []
        this_start = self.start
        for letter in name:
            this_end = self.letters_map.get(letter)
            if not this_end:
                raise ValueError('Unknown symbol: %s', letter)

            if this_start == this_end:
                continue
            this_sequence = self._resolve_step(this_start, this_end)
            result.extend(this_sequence)
            this_start = this_end
        return result

    def _resolve_step(self, source, destination):
        source_x, source_y = source
        dest_x, dest_y = destination

        # validation
        assert source_x < self.rows
        assert dest_x < self.rows
        assert source_y < self.columns
        assert dest_y < self.columns

        result = []
        x_diff = source_x - dest_x
        if x_diff < 0:
            result.extend(['DOWN'] * abs(x_diff))
        elif x_diff > 0:
            result.extend(['UP'] * abs(x_diff))

        y_diff = source_y - dest_y
        if y_diff < 0:
            result.extend(['RIGHT'] * abs(y_diff))
        elif y_diff > 0:
            result.extend(['LEFT'] * abs(y_diff))

        return result


if __name__ == "__main__":
    print Solution().to_commands('XZ')
