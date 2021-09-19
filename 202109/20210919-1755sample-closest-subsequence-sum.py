from bisect import *


class Solution:
  def minAbsDifference(self, nums: List[int], goal: int) -> int:
    n = len(nums)
    nums = sorted(nums)
    hLen = (n + 1) >> 1

    def getSum(curr, i, j, s):
      if i >= j:
        s.add(curr)
        return

      getSum(curr, i + 1, j, s)
      getSum(curr + nums[i], i + 1, j, s)

    s1 = set()
    s2 = set()

    getSum(0, 0, hLen, s1)
    getSum(0, hLen, n, s2)

    arr2 = sorted([*s2])
    l2 = len(arr2)
    res = abs(goal)

    for sub in s1:
      i = bisect(arr2, goal - sub)

      for j in range(max(0, i - 1), min(l2, i + 1)):
        res = min(res, abs(sub + arr2[j] - goal))

    return res
