class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    h = defaultdict(int)
    h[0] = 1
    summ = sum(nums)

    for num in nums:
      h |= {key + num: (h[key + num] if key + num in h else 0) + h[key]
            for key in h}

    key = (summ - target) >> 1

    if key * 2 != summ - target:
      return 0

    return h[key]
