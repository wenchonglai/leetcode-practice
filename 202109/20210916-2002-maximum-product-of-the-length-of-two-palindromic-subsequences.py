class Solution:
  def maxProduct(self, s: str) -> int:
    @cache
    def longestPal(s):
      n = len(s)

      if n < 2:
        return n

      if s[0] == s[-1]:
        return longestPal(s[1:-1]) + 2

      return max(longestPal(s[1:]), longestPal(s[:-1]))

    @cache
    def dfs(s1, s2, i):
      if not s2:
        return 0

      res = longestPal(s1) * longestPal(s2)

      for j in range(i, len(s2)):
        val = dfs(s1 + s2[j], s2[:j] + s2[j + 1:], j)

        if val > res:
          res = val

      return res

    return dfs(s[0], s[1:], 0)
