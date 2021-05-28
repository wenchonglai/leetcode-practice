class Solution:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    l1 = 0
    l2 = 0
    ct = 0
    res = 0
    N = len(nums)

    for i in range(0, N):
      ct += nums[i]

      while nums[l2] == 0 and l2 < i:
        l2 += 1

      if ct > goal:
        ct -= 1
        l1, l2 = l2 + 1, l2 + 1

        while l2 < i and nums[l2] == 0:
          l2 += 1

      if ct == goal and i >= l2:
        res += l2 - l1 + 1

    return res