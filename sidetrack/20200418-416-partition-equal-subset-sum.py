class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    N = len(nums)
    _sum = sum(nums)

    if _sum % 2 == 1:
      return False

    half_s = _sum // 2
    s = {0}

    for num in nums:
      for n in list(s):
        if n + num == half_s:
          return True
        s.add(n + num)

    return False
