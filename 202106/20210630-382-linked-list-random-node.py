# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.curr = head
        self.curr2 = head
        self.ct = 1

        node = head

        while node.next:
          self.ct += 1
          node = node.next

        for i in range(random.randint(0, self.ct - 1)):
          self.curr2 = self.curr2.next

        node.next = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if random.randint(0, 1) == 0:
          self.curr = self.curr.next
          self.curr2.val, self.head.val = self.head.val, self.curr2.val
        if random.randint(0, 1) == 0:
          self.curr2 = self.curr2.next
          self.curr.val, self.curr2.val = self.curr2.val, self.curr.val

        return self.curr.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
