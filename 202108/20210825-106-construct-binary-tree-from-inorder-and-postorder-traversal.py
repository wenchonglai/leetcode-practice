# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    h = {}
    for (i, num) in enumerate(inorder):
      h[num] = i

    def helper(l, r):
      if l > r:
        return None

      val = postorder.pop()
      idx = h[val]
      r = helper(idx + 1, r)
      l = helper(l, idx - 1)

      return TreeNode(val, l, r)

    return helper(0, len(inorder) - 1)
