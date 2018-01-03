import collections

"""Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order comes first.

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
    
Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Input words contain only lowercase letters.
"""


class MinOfMaxHeap(object):
    """Represents collection of k top frequent elements with minimum on top."""
    def __init__(self, size):
        self.size = size
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def min(self):
        if self.is_empty():
            raise Exception('Heap is empty')

        return self.data[0]

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
        # move up if new < parent
        if j > 0 and self.data[j] < self.data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left_ind = self._left(j)
            small_child = left_ind
            if self._has_right(j):
                right_ind = self._right(j)
                if self.data[right_ind] < self.data[left_ind]:
                    small_child = right_ind
            # move down if children < new
            if self.data[small_child] < self.data[j]:
                self._swap(small_child, j)
                self._downheap(small_child)

    def remove_min(self):
        if self.is_empty():
            raise Exception('Heap is empty')

        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._downheap(0)
        return item

    def add(self, elem):
        """Add new element to MinOfMaxHeap.

        If heap is already full and new element is greater than the top element,
        remove it and add new element.
        """
        if len(self) < self.size:
            self.data.append(elem)
            self._upheap(len(self.data) - 1)
        else:
            min_so_far = self.min()
            if elem > min_so_far:
                self.remove_min()
                self.data.append(elem)
                self._upheap(len(self.data) - 1)


class Solution(object):
    class _Item(object):
        def __init__(self, count, word):
            self._count = count
            self._word = word

        def __str__(self):
            return '%s' % self._word

        def __gt__(self, other):
            return (
                self._count > other._count or
                # check alphabetical order of word
                (self._count == other._count and self._word < other._word))

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words:
            raise ValueError

        words_count = collections.defaultdict(int)
        for word in words:
            words_count[word] += 1

        items = []
        for word, count in words_count.iteritems():
            items.append(self._Item(count, word))

        h = MinOfMaxHeap(k)
        for item in items:
            h.add(item)

        result = []
        while h:
            result.append(h.remove_min())

        return [str(elem) for elem in result[::-1]]


if __name__ == '__main__':
    print Solution().topKFrequent(
        ["i", "love", "leetcode", "i", "love", "coding"], 1)

    print Solution().topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
        4)

    print Solution().topKFrequent(
        ["abc", "abc", "ac", "ac", "ac", "bca", "bca", "bca", "bca", "abc"],
        3)
