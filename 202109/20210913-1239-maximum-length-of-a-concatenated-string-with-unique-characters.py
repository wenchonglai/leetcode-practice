class Solution:
  def maxLength(self, arr: List[str]) -> int:
    n = len(arr)

    @cache
    def dfs(curr, nxtI):
      nonlocal n
      res = len(curr)

      if res >= 26:
        return res

      if nxtI == n:
        return res

      for (j, word) in enumerate(arr[nxtI:]):
        if len(curr + word) == len(set([*curr, *word])):
          val = dfs(curr + word, nxtI + j)
          res = max(res, val)

      return res

    return dfs("", 0)
