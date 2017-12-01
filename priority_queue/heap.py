def is_kth_smallest_greater_x(min_heap, k, x):
    """
    Given an array-based heap on n elements and a real number x,
    determine of the kth smallest in the heap is greater than or equal to x
    """
    count = 0
    this_level = [0]
    while this_level:
        next_level = []
        for i in this_level:
            if min_heap.data[i] <= x:
                count += 1
                if count >= k:
                    return i

                if min_heap._has_left(i):
                    next_level.append(min_heap._left(i))

                if min_heap._has_right(i):
                    next_level.append(min_heap._right(i))

        this_level = next_level

    return -1


class MinHeap(object):
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self.data)

    def _has_right(self, j):
        return self._right(j) < len(self.data)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left_ind = self._left(j)
            smallest_ind = left_ind
            if self._has_right(j):
                right_ind = self._right(j)
                if self.data[right_ind] < self.data[left_ind]:
                    smallest_ind = right_ind

            if self.data[smallest_ind] < self.data[j]:
                self._right(smallest_ind, j)
                self._downheap(smallest_ind)

    def add(self, elem):
        self.data.append(elem)
        self._upheap(len(self.data) - 1)

    def remove_min(self):
        if self.is_empty():
            raise Exception('Heap is empty')

        self._swap(0, len(self.data) - 1)
        min_ = self.data.pop()
        self._downheap(0)
        return min_


if __name__ == '__main__':
    h = MinHeap()
    for elem in (7, 5, 0, 1, 6, 2):
        h.add(elem)

    print h

    print is_kth_smallest_greater_x(h, 3, 3)
