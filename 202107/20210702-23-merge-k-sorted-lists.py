class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    K = len(lists)

    if K == 0:
      return

    if K == 1:
      return lists[0]

    def helper(l1, l2):
      p1 = l1
      p2 = l2
      head = ListNode()
      p = head

      while p1 and p2:
        if p1.val < p2.val:
          p.next = p1
          p1 = p1.next
        else:
          p.next = p2
          p2 = p2.next

        p = p.next

      p.next = p1 if p1 else p2

      return head.next

    return self.mergeKLists(
        [helper(lists[i * 2], lists[i * 2 + 1]) for i in range(K >> 1)] +
        ([] if K % 2 == 0 else [lists[-1]])
    )
