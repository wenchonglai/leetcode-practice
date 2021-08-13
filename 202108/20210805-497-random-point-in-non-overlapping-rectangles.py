class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.acc = [0]

        for [x1, y1, x2, y2] in rects:
          self.acc.append((x2 - x1 + 1) * (y2 - y1 + 1) + self.acc[-1])

    def pick(self) -> List[int]:
      idx = randint(0, self.acc[-1] - 1)
      i = bisect.bisect(self.acc, idx) - 1
      [x1, y1, x2, y2] = self.rects[i]
      delta = x2 - x1 + 1
      residual = idx - self.acc[i]

      return [x1 + residual % delta, y1 + residual // delta]
