class Solution:
  def findBestValue(self, arr: List[int], target: int) -> int:
    sarr = sorted(arr)
    N = len(arr)
    l = 0
    r = sarr[-1]
    min_ = 10 ** 5
    res = None

    while l <= r:
      m = l + r >> 1
      i = bisect_left(sarr, m)
      diff = sum(sarr[0:i]) + (N - i) * m - target

      if diff == 0:
        return m
      elif diff > 0:
        r = m
      else:
        l = m + 1

      abs_ = abs(diff)

      if abs_ == min_ and res and m < res:
        res = m

      if abs_ < min_:
        res = m
        min_ = abs_

      if l == m and r == m:
        break

    return res