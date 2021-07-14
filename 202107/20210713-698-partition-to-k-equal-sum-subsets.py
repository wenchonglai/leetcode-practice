class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    N = len(nums)
    s = sum(nums)

    if s % k != 0:
      return False

    nums = sorted(nums)

    @cache
    def dfs(n, tup):
      l = list(tup)

      if n == 0:
        if l:
          return dfs(s // k, tup)
        return True

      for (i, num) in enumerate(l):
        if n - num >= 0:
          val = dfs(n - num, tuple(l[:i] + l[i + 1:]))

          if val:
            return val

    return dfs(s // k, tuple(nums))
