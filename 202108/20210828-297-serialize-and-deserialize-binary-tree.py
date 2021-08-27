# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:
  def serialize(self, root):
      """Encodes a tree to a single string.

      :type root: TreeNode
      :rtype: str
      """
      if not root:
        return "-"

      q = [root]
      res = [root.val]

      while q:
        _q = []

        for node in q:
          if node.left:
            _q.append(node.left)
            res.append(node.left.val)
          else:
            res.append('-')

          if node.right:
            _q.append(node.right)
            res.append(node.right.val)
          else:
            res.append('-')

        q = _q

      return ','.join([str(el) for el in res])

  def deserialize(self, data):
    nodes = [None if el == '-' else TreeNode(int(el))
             for el in data.split(',')]

    if not nodes:
      return None

    root = nodes[0]
    q = deque([root])
    ct = 0

    for node in nodes[1:]:
      if ct == 2:
        q.popleft()
        ct = 0

      if ct == 1:
        q[0].right = node
      else:
        q[0].left = node

      if node:
        q.append(node)

      ct += 1

    return root


"""Decodes your encoded data to tree.

:type data: str
:rtype: TreeNode
"""


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
