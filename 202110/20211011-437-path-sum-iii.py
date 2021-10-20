# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: TreeNode, targetSum: int) -> int:
    if root == None:
      return 0

    h = {0: 1}

    def dfs(node, acc):
      res = 0
      nonlocal h

      if node == None:
        return 0

      acc += node.val

      if acc not in h:
        h[acc] = 0

      h[acc] += 1

      if acc - targetSum in h:
        res += h[acc - targetSum]

      res += dfs(node.left, acc) + dfs(node.right, acc)
      h[acc] -= 1

      return res - 1 if targetSum == 0 else res

    val = dfs(root, 0)

    return val
