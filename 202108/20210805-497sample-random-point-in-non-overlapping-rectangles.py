class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.acc = [0]

        for [x1, y1, x2, y2] in rects:
          self.acc.append((x2 - x1 + 1) * (y2 - y1 + 1) + self.acc[-1]) # note: why x2 - x1 + 1 and y2 - y1 + 1?

    def pick(self) -> List[int]:
      idx = randint(0, self.acc[-1] - 1)    # note: why minus 1?
      i = bisect.bisect(self.acc, idx) - 1  # note: why bisect and not bisect_left?
      [x1, y1, x2, y2] = self.rects[i]
      delta = x2 - x1 + 1
      residual = idx - self.acc[i]

      return [x1 + residual % delta, y1 + residual // delta]
