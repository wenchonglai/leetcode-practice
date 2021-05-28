class Solution:
  def getMaxLen(self, nums: List[int]) -> int:
    h = {-1: [], 1: [0]}
    m = 0
    sign = 1

    for i in range(len(nums)):
      num = nums[i]

      if num == 0:
        max_pos = (h[1][-1] - h[1][0]) if h[1] else 0
        max_neg = (h[-1][-1] - h[-1][0]) if h[-1] else 0
        m = max(max_pos, max_neg, m)

        h = {-1: [], 1: [i + 1]}
        sign = 1
      else:
        if num < 0:
          sign *= -1

        h[sign].append(i + 1)

    max_pos = (h[1][-1] - h[1][0]) if h[1] else 0
    max_neg = (h[-1][-1] - h[-1][0]) if h[-1] else 0
    m = max(max_pos, max_neg, m)

    return m