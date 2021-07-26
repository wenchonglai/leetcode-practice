from bisect import bisect


class Solution:
  arr = [2 ** i for i in range(32)]

  @cache
  def findIntegers(self, n: int) -> int:
    if n == 0:
      return 1
    if n == 1:
      return 2
    if n == 2:
      return 3

    base = self.arr[bisect(self.arr, n) - 1]
    residual = n - base

    if residual == 0:
      return self.findIntegers(base // 2 - 1) + self.findIntegers(base // 4)
    elif residual * 2 >= base:
      return self.findIntegers(base - 1) + self.findIntegers(base // 2 - 1)
    else:
      return self.findIntegers(base - 1) + self.findIntegers(residual)
