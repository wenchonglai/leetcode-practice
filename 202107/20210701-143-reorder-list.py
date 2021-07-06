class Solution:
  def reorderList(self, head: ListNode) -> None:
    p21 = head
    p22 = head

    while p22 and p22.next and p22.next.next:
      p21 = p21.next
      p22 = p22.next.next

    p22 = p21.next

    while p22 and p22.next:
      p23 = p22.next
      p21.next, p22.next, p23.next = p23, p23.next, p21.next

    p11 = head
    while p21 != p11:
      p22 = p21.next
      p11.next, p22.next, p21.next, p11 = p22, p11.next, p22.next, p11.next
