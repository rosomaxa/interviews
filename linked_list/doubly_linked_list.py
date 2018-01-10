class _DoublyLinkedBase(object):

    class _Node(object):
        def __init__(self, element, next_, prev):
            self._element = element
            self._next = next_
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def _insert_between(self, element, predecessor, successor):
        new = self._Node(element, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._element = node._next = node._prev = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise ValueError('Deque is empty')

        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise ValueError('Deque is empty')

        return self._trailer._prev._element

    def insert_first(self, element):
        return self._insert_between(element, self._header, self._header._next)

    def insert_last(self, element):
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise ValueError('Deque is empty')

        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise ValueError('Deque is empty')

        return self._delete_node(self._trailer._prev)
