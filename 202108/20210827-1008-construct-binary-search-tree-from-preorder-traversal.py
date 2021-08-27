# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    stack = []
    root = None
    node = root

    for num in preorder:
      if not stack or num < stack[-1].val:
        if not root:
          root = TreeNode(num)
          node = root
        else:
          node.left = TreeNode(num)
          node = node.left
      else:
        while stack and num > stack[-1].val:
          node = stack.pop()

        if node:
          node.right = TreeNode(num)
          node = node.right

      stack.append(node)

    return root
