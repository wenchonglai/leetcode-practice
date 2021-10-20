class Solution:
  def new21Game(self, n: int, k: int, maxPts: int) -> float:
    if k + maxPts - 1 <= n:
      return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    acc = 0

    for i in range(1, k + 1):
      acc += dp[i - 1]

      if i - maxPts - 1 >= 0:
        acc -= dp[i - maxPts - 1]

      dp[i] = acc / maxPts

    for i in range(k + 1, n + 1):
      if i - maxPts - 1 >= 0:
        acc -= dp[i - maxPts - 1]

      dp[i] = acc / maxPts

    return sum(dp[k:])
