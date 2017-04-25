def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
    return root


# class Node(object):
#     def __init__(self, data=None, left=None, right=None):
#         self.left, self.right = left, right
#         self.data = data

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

# def is_bst():
