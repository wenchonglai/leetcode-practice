class Solution:
  def splitArraySameAverage(self, nums: List[int]) -> bool:
    s = set()
    n = len(nums)
    summ = sum(nums)
    nums = [num * n - summ for num in sorted(nums)]

    for num in nums[0:-1]:
      s |= ({num} if num <= 0 else set()) | {
          el + num for el in s if el + num <= 0}

      if 0 in s:
        return True

    return False
