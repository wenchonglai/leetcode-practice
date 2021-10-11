class Solution:
  def rob(self, nums: List[int]) -> int:
    res = [0, 0]

    for num in nums:
      res.append(max(res[-2] + num, res[-1]))

    return max(res)