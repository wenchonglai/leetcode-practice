class Solution:
  def tallestBillboard(self, rods: List[int]) -> int:
    half = min(sum(rods), 2500)

    @cache
    def dfs(i, balance):
      if i == len(rods) or abs(balance) > half:
        return 0 if balance == 0 else -float("inf")

      rod = rods[i]

      return max(
          dfs(i + 1, balance),
          rod + dfs(i + 1, balance + rod),
          rod + dfs(i + 1, balance - rod)
      )

    return dfs(0, 0) >> 1
