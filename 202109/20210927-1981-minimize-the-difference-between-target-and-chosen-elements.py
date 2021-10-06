class Solution:
  def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
    n, m = len(mat), len(mat[0])

    @cache
    def dp(i, t):
      if t < 0:
        return False

      if i == n:
        return t == 0

      for v in mat[i]:
        if dp(i + 1, t - v):
          return True

      return False

    max_ = sum([max(sub) for sub in mat])
    res = abs(target - max_)
    l, r = n, max_ + 1

    while r >= l:
      for val in range(l, r):
        if dp(0, val) and (res == None or abs(target - val) < res):
          res = abs(target - val)
          l = max(l, target - val)
          r = min(r, target + val + 1)
          break

      if val == r:
        return res
      l += 1

    return res
