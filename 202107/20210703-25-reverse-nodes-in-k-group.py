# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    sentinel = ListNode(None, head)
    p1 = sentinel

    while p1:
      p = p1

      for i in range(k):
        p = p.next

        if not p:
          return sentinel.next

      p2 = p1.next

      for i in range(k - 1):
        p3 = p2.next

        if not p3:
          return sentinel.next

        p1.next, p3.next, p2.next = p3, p1.next, p3.next

      p1 = p2

    return sentinel.next
