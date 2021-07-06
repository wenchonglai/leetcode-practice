class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    zeros = 0
    prodAll = 1
    N = len(nums)

    for num in nums:
      prodAll *= num if num != 0 else 1
      zeros += 1 if num == 0 else 0

    if zeros > 1:
      return [0] * N

    if zeros == 1:
      return [prodAll if num == 0 else 0 for num in nums]

    return [prodAll // num for num in nums]
