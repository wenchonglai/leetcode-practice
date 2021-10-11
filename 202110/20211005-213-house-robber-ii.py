class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) < 2:
      return nums[0]

    res = [0, 0]

    for num in nums[:-1]:
      res.append(max(res[-2] + num, res[-1]))

    m1 = max(res)

    res = [0, 0]

    for num in nums[1:]:
      res.append(max(res[-2] + num, res[-1]))

    m2 = max(res)

    return max(m1, m2)
