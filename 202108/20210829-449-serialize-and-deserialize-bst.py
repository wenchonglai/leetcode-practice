# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        stack = []

        def dfs(node):
          nonlocal stack

          if not node:
            return

          stack.append(str(node.val))
          dfs(node.left)
          dfs(node.right)

        if not root:
          return ''

        dfs(root)

        return ','.join(stack)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
          return None

        nodes = [TreeNode(int(el)) for el in data.split(',')]
        last = nodes[0]
        stack = []

        for node in nodes[1:]:

          if node.val < last.val:
            last.left = node
            stack.append(last)

          else:
            while stack and node.val > stack[-1].val:
              last = stack.pop()

            last.right = node

          last = node

        return nodes[0]


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
