class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    """
    Left, Root, Right
    """
    if root:
        inorder(root.left)
        print (root.value)
        inorder(root.right)


def preorder(root):
    """
    Root, Left, Right
    """
    if root:
        print (root.value)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """
    Left, Right, Root
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print (root.value)
