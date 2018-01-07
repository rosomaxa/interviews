class Empty(Exception):
    pass


class LinkedList(object):
    class _Node(object):
        def __init__(self, element, next_=None):
            self._element = element
            self._next = next_

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Empty('%s is empty.' % self.__class__.__name__)

        return self._head._element


class LinkedStack(LinkedList):
    """All of the methods complete in worst-case constant time."""

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        top = self.top()
        self._head = self._head._next
        self._size -= 1
        return top


class LinkedQueue(LinkedList):
    """All of the methods complete in worst-case constant time."""

    def __init__(self):
        """Since we need to perform operations on both ends of the queue,
        we will explicitly maintain both a _head and a _tail references."""
        super(LinkedQueue, self).__init__()
        self._tail = None

    def dequeue(self):
        top = self.top()
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

        return top

    def enqueue(self, e):
        new = self._Node(e)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1


class CircularLinkedQueue(LinkedList):
    def __init__(self):
        super(CircularLinkedQueue, self).__init__()
        del self._head
        self._tail = None

    def top(self):
        if self.is_empty():
            raise Empty('%s is empty' % self.__class__.__name__)

        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        if len(self) == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element

    def enqueue(self, e):
        new = self._Node(e)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def rotate(self):
        if len(self) > 0:
            self._tail = self._tail._next
