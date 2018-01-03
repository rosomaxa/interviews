class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_levels(root):
    stack = [[root]]
    levels = []
    while stack:
        this_vals = []
        this_level = stack.pop()
        next_level = []
        for node in this_level:
            this_vals.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            stack.append(next_level)
        levels.append(this_vals)
    return levels


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)

    levels = get_levels(root)
    for level in levels:
        print level
