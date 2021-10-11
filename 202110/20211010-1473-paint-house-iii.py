class Solution:
  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    @cache
    def dp(ct, y, x):
      hi = houses[y] - 1
      res = None

      if y < ct - 1:
        return res

      if hi >= 0 and x != hi:
        return res

      if ct == 1 and y == 0:
        return 0 if hi >= 0 else cost[y][x]

      if ct < 1:
        return res

      c = cost[y][x] if hi == -1 else 0

      for i in range(n):
        val = dp(ct + (0 if i == x else -1), y - 1, i)
        temp = val + c if val != None else None

        if temp != None and (res == None or temp < res):
          res = temp

      return res

    res = -1

    for x in range(n):
      temp = dp(target, m - 1, x)
      if temp != None and (res == -1 or temp < res):
        res = temp

    return res
