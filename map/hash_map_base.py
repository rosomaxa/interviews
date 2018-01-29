"""
Collision-Handling Schemes:
- Separate Chaining
- Open Addressing:
-- Linear Probing
-- Quadratic Probing;
-- Double Hashing (use of secondary hash function)
"""
import abc
import random

from interviews.map import map_base


class HashMapBase(map_base.MapBase):
    def __init__(self, capacity=11, p=109345121):
        self._table = [None] * capacity
        self._n = 0  # number of entries in the map
        self._prime = p  # prime for MAD compression
        self._scale = 1 + random.randrange(p - 1)
        self._shift = random.randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale +
                self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    @abc.abstractmethod
    def _bucket_getitem(self, j, k):
        pass

    @abc.abstractmethod
    def _bucket_setitem(self, j, k, v):
        pass

    @abc.abstractmethod
    def _bucket_delitem(self, j, k):
        pass

    @abc.abstractmethod
    def __iter__(self):
        pass

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = [None] * c
        self._n = 0
        for k, v in old:
            self[k] = v
