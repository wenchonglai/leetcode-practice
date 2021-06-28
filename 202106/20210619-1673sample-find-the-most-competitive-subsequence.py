class Solution:
  def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    stack = []
    i = len(nums) - k

    for val in nums:
      while i > 0 and stack and val < stack[-1]:
        stack.pop()
        i -= 1

      stack.append(val)

    return stack[:k]
