class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    N = len(nums)
    max_ = nums[0]
    pos = 0
    neg = 0

    for num in nums:
      if num >= 0:
        pos += num
      else:
        neg += num

      max_ = max(pos + neg, max_)

      if pos + neg < 0:
        pos = 0
        neg = 0

    return max_
