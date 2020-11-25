# Time Complexity: O(n) worst case

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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


def lca_values(root, value1, value2):
    try:
        node1 = get_node(root, value1)
        node2 = get_node(root, value2)
    except KeyError:
        raise
    else:
        return lca_nodes(root, node1, node2).value

def lca_nodes(root, node1, node2):
    if not root:
        return
    if node1.value == root.value or node2.value == root.value:
        return root
    left = lca_nodes(root.left, node1, node2)
    right = lca_nodes(root.right, node1, node2)

    if left and right:
        return root

    if left:
        return left

    return right
