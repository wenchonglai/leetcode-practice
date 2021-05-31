class Solution:
  def minOperations(self, nums: List[int], x: int) -> int:
    # prefix sum
    # 先算出所有nums的和，然后遍历所有nums，
    # 当prefix sum大于x时，不断减去prefix sum的开头项，
    # 直至新的prefix sum小于等于x
    target = sum(nums) - x
    N = len(nums)

    if target == 0:
      return N
    elif target < 0:
      return -1
    elif x == 0:
      return 0

    s = 0
    m = N
    j = 0

    for i in range(0, N):
      s += nums[i]

      while s > target:
        s -= nums[j]
        j += 1

      if s == target and N - i + j - 1 < m:
        m = N - i + j - 1

    return -1 if m >= N else m
