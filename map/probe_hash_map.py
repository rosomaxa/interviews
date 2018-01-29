from interviews.map import hash_map_base


class ProbeHashMap(hash_map_base.HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    # Special marker for deleted locations.
    # In case of collisions if several keys were taken and later something
    # ont he middle has been removed and we search for something placed after
    # this deleted location, we should distinguish between locations that were
    # never taken and keep searching until we either find a match or truly
    # untaken location.
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        
        Return (success, index) tuple, described as follows.
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available
        slot.
        """
        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j
                if self._table[j] is None:
                    return False, first_avail

            elif k == self._table[j]._key:
                return True, j

            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))

        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))

        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in xrange(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
