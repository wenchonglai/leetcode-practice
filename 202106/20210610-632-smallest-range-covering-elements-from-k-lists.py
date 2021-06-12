from heapq import *


class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    k = len(nums)
    indices = [0] * k
    h = []
    hi = -10 ** 5

    for (i, sub) in enumerate(nums):
      h.append((sub[0], i))

    heapify(h)
    hi = max([num for (num, i) in h])
    lo = h[0][0]
    res = []

    while True:
      num, i = heappop(h)
      lo = num
      idx = indices[i]

      if not res or hi - lo < res[-1] - res[0]:
        res = [lo, hi]

      if len(nums[i]) > idx + 1:
        indices[i] += 1
        newNum = nums[i][idx + 1]
        heappush(h, (newNum, i))

        if newNum > hi:
          hi = newNum
      else:
        return res
