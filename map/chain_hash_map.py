from interviews.map import hash_map_base
from interviews.map import unsorted_table_map


class ChainHashMap(hash_map_base.HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))

        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = unsorted_table_map.UnsortedTableMap()
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))

        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for k in bucket:
                    yield k
