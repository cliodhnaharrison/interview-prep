# Time Complexity: O(n) worst case

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def get_node(root, value):
    if not root:
        raise KeyError("Key {} not found in tree.".format(value))

    if root.value == value:
        return root

    try:
        left_result = get_node(root.left, value)
        return left_result
    except KeyError:
        return get_node(root.right, value)


def ancestors(root, value):
    try:
        node = get_node(root, value)
    except KeyError:
        return []
    else:
        node_ancestors = []
        while node.parent:
            node_ancestors.append(node.parent.value)
            node = node.parent
        return node_ancestors
