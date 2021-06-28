class Solution:
  def validSubarrays(self, nums):
    N = len(nums)
    stack = []
    counts = (N * N + N) // 2

    for (i, num) in enumerate(nums):

      while stack and nums[stack[-1]] > num:
        stack.pop()
        counts -= N - i

      stack.append(i)
    
    return counts