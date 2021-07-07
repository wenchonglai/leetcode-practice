from bisect import bisect
from random import random


class Solution:

    def __init__(self, w: List[int]):
      self.sorted = sorted([(num, i) for (i, num) in enumerate(w)])
      self.acc = [0]

      for (num, i) in self.sorted:
        self.acc.append(num + self.acc[-1])

      self.max = self.acc[-1]

    def pickIndex(self) -> int:
        rand = random() * self.max
        i = bisect(self.acc, rand) - 1
        return self.sorted[i][1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
