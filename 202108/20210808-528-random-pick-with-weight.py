class Solution:

    def __init__(self, w: List[int]):
        self.arr = w
        self.acc = [0]

        for w in self.arr:
          self.acc.append(self.acc[-1] + w)

    def pickIndex(self) -> int:
        total = self.acc[-1]
        val = randint(0, total - 1)
        idx = bisect.bisect(self.acc, val) - 1

        return idx
