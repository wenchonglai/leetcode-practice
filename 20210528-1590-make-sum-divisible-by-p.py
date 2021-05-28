class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    N = len(nums)
    i = 0
    s = 0
    h = {0: 0}
    mod = sum(nums) % p
    m = N

    for num in nums:
      i += 1
      s = (s + num) % p
      h[s] = i
      corr = (s + p - mod) % p

      if corr in h and i - h[corr] < m:
        m = i - h[corr]

    return m if m < N else -1