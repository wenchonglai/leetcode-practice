class Solution:
  def lastStoneWeightII(self, stones: List[int]) -> int:
    summ = sum(stones)
    s = {0}

    for stone in stones:
      s |= {stone + el for el in s}

    return min(abs(summ - el * 2) for el in s)
