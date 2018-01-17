import abc

from interviews.tree.tree_adt import tree_base


class BinaryTree(tree_base.Tree):
    @abc.abstractmethod
    def left(self, p):
        pass

    @abc.abstractmethod
    def right(self, p):
        pass

    def subling(self, p):
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
