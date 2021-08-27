# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    h = {}
    preorder = preorder[::-1]

    for (i, num) in enumerate(inorder):
      h[num] = i

    def helper(l, r):
      if l > r:
        return None

      rootVal = preorder.pop()
      idx = h[rootVal]

      return TreeNode(
          rootVal,
          helper(l, idx - 1),
          helper(idx + 1, r)
      )

    return helper(0, len(inorder) - 1)
