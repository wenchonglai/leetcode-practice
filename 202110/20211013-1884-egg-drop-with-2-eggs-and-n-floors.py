class Solution:
  def twoEggDrop(self, floors: int) -> int:
    dp = [0, 1, 3]

    if floors < 2:
      return dp[floors]

    while dp[-1] < floors:
      dp.append(dp[-1] * 2 - dp[-2] + 1)

    return len(dp) - 1
