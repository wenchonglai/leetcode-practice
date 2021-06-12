from collections import deque
from sortedcontainers import SortedList
from bisect import bisect, bisect_right


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.len = 0
        self.dq = deque()
        self.sarr = SortedList()
        self.s1 = 0
        self.s2 = 0

    def addElement(self, num: int) -> None:
      i2 = self.m - self.k
      i1 = self.k

      self.dq.append(num)
      nIndex = bisect_right(self.sarr, num)

      if nIndex < i2:
        self.s2 += num

        if self.len >= i2:
          self.s2 -= self.sarr[i2 - 1]

        if nIndex < i1:
          self.s1 += num

          if self.len >= i1:
            self.s1 -= self.sarr[i1 - 1]

      self.sarr.add(num)

      if self.len == self.m:
        popped = self.dq.popleft()
        pIndex = bisect_left(self.sarr, popped)

        if pIndex < i2:
          self.s2 += self.sarr[i2] - popped

          if pIndex < i1:
            self.s1 += self.sarr[i1] - popped

        self.sarr.remove(popped)
      else:
        self.len += 1

    def calculateMKAverage(self) -> int:
      return (self.s2 - self.s1) // (self.m - 2 * self.k) if self.len == self.m else -1