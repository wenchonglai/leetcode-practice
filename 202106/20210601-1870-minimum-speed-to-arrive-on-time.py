class Solution:
  def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
    def calcTime(speed):
      h = 0

      for d in dist:
        h += (d - 1) // speed + 1

      if dist[-1] % speed != 0:
        h = h - 1 + (dist[-1] % speed) / speed

      return h

    N = len(dist)

    if N > hour + 1:
      return -1

    l = 1
    R = max(dist) * 100
    r = R

    while l < r:
      m = l + r >> 1
      h = calcTime(m)

      if h == hour:
        return m
      elif h > hour:
        l = m + 1
      elif h < hour:
        r = m - 1

    if calcTime(l) > hour:
      l += 1

    return l if l <= R else -1
