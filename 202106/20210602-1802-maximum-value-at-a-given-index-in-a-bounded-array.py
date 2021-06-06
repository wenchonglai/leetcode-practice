class Solution:
  def maxValue(self, n: int, index: int, maxSum: int) -> int:

    def calMaxVal(maxNum):
      s = 0

      if maxNum <= index:
        s += (maxNum - 1) * maxNum // 2 + index + 1
      else:
        s += (maxNum * 2 - index) * (index + 1) // 2

      if maxNum <= n - 1 - index:
        s += (maxNum - 1) * maxNum // 2 + n - index
      else:
        s += (maxNum * 2 - n + index + 1) * (n - index) // 2

      return s - maxNum

    lo = 1
    hi = n + (maxSum - 1) // n + 1

    while lo < hi:
      m = lo + hi >> 1
      val = calMaxVal(m)

      if val == maxSum:
        return m
      elif val > maxSum:
        hi = m - 1
      else:
        lo = m + 1

    val = calMaxVal(lo)

    return lo - 1 if val > maxSum else lo
