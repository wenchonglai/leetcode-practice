from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self.h = defaultdict(list)

        for (i, num) in enumerate(nums):
          self.h[num].append(i)

    def pick(self, target: int) -> int:
      return self.h[target][randint(0, len(self.h[target]) - 1)]
