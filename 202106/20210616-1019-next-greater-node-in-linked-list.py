# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def nextLargerNodes(self, head: ListNode) -> List[int]:
    res = []
    node = head

    while node:
      res.append(node.val)
      node = node.next

    stack = [0]

    for i in range(len(res) - 1, -1, -1):
      val = res[i]

      while stack[-1] != 0 and stack[-1] <= val:
        stack.pop()

      res[i] = stack[-1]
      stack.append(val)

    return res
