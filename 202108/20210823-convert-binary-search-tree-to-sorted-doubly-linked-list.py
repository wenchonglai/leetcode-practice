"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        # Write your code here.
        self.sentinel = TreeNode(None)
        self.node = self.sentinel

        def insort(node):
            if node.left:
                insort(node.left)

            newNode = TreeNode(node.val)
            newNode.left = self.node
            self.node.right = newNode
            self.node = newNode

            if node.right:
                insort(node.right)

        insort(root)

        if not self.sentinel.right:
            return None

        self.node.right = self.sentinel.right
        self.sentinel.right.left = self.node

        return self.sentinel.right
