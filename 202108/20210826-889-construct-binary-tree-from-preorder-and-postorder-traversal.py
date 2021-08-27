# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        h = {}
        h2 = {}
        postorder = postorder[::-1]

        for (i, num) in enumerate(preorder):
          h[num] = i
          h2[postorder[i]] = i

        def helper(s1, e1):
          if s1 > e1:
            return None

          if s1 == e1:
            return TreeNode(preorder[s1], None, None)

          val = preorder[s1]
          nextS1 = s1 + 1
          nextE1 = h[postorder[h2[val] + 1]] - 1

          return TreeNode(
              val,
              helper(nextS1, nextE1),
              helper(nextE1 + 1, e1)
          )

        return helper(0, len(postorder) - 1)
