import abc


class Tree(object):
    class Position(object):
        """An abstraction representing the location of a single element."""

        @abc.abstractmethod
        def element(self):
            pass

        @abc.abstractmethod
        def __eq__(self, other):
            pass

        def __ne__(self, other):
            return not self == other

    @abc.abstractmethod
    def root(self):
        pass

    @abc.abstractmethod
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        pass

    @abc.abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""
        pass

    @abc.abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        pass

    @abc.abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        pass

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0

        return 1 + self.depth(self.parent(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        def _height(node):
            if self.is_leaf(node):
                return 0

            return 1 + max(_height(c) for c in self.children(node))

        if p is None:
            p = self.root()

        return _height(p)


class BinaryTree(Tree):
    @abc.abstractmethod
    def left(self, p):
        pass

    @abc.abstractmethod
    def right(self, p):
        pass

    def sibling(self, p):
        """Return a Position representing p's sibling (None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return

        if p == self.left(parent):
            return self.right(parent)

        return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
