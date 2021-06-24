class Solution:
  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

    n0 = ListNode(None, head)
    n1 = n0.next
    n = n0
    delta = right - left

    while left > 1:
      left -= 1
      n0 = n0.next
      n1 = n0.next

    n2 = n1
    n3 = n2.next

    while delta > 0:
      n1, n3.next, n3, n0.next, n2.next = n3, n1, n3.next, n3, n3.next
      delta -= 1

    return n.next
