from collections import deque

class Solution:
  def minSideJumps(self, obstacles: List[int]) -> int:
    INF = float("inf")
    a, b, c = INF, 0, INF

    for (i, ob) in enumerate(obstacles):
      if ob == 0:
        a, b, c = min(min(b, c) + 1, a), min(min(a, c) +
                                             1, b), min(min(b, a) + 1, c)

      elif ob == 1:
        a, b, c = INF, min(c + 1, b), min(b + 1, c)

      elif ob == 2:
        a, b, c = min(c + 1, a), INF, min(a + 1, c)

      elif ob == 3:
        a, b, c = min(b + 1, a), min(a + 1, b), INF

    return min(a, b, c)
