from interviews.map import map_base


class UnsortedTableMap(map_base.MapBase):
    """Simple, but inefficient map.
    
    ALl methods run in O(n).
    """
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value

        raise KeyError(repr(k) + ' not found.')

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return

        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for i, item in enumerate(self._table):
            if k == item._key:
                self._table.pop(i)
                return

        raise KeyError(repr(k) + ' not found.')

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key
