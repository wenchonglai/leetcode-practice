class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    N = len(nums)

    if N == 1:
      return 0

    l, r = None, 0
    stack = []
    _max = nums[0]

    for (i, num) in enumerate(nums):
      if num < _max:
        r = i
        while stack and stack[-1][1] > num:
          if l is not None:
            l = min(l, stack[-1][0])
          else:
            l = stack[-1][0]
          stack.pop()
      else:
        _max = num
        stack.append((i, num))

    if l is None:
      return 0

    return r - l + 1
