class Solution:
  def specialArray(self, nums: List[int]) -> int:
    N = len(nums)

    if N == 0:
      return -1

    if N == 1:
      return 1 if nums[0] >= 1 else -1

    snums = sorted(nums, reverse=True)

    for i in range(1, N):
      num = snums[i]

      if num != snums[i - 1]:
        if i <= snums[i - 1] and i > num:
          return i

    return i + 1 if i + 1 <= snums[-1] else -1
