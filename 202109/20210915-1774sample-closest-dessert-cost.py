from bisect import bisect_left

class Solution:
  def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    baseCosts = sorted(baseCosts)
    toppingCosts = sorted(toppingCosts, reverse=True)
    n, m = len(baseCosts), len(toppingCosts)
    res = None

    def gen(i=m - 1):
      num = toppingCosts[i]

      if i == 0:
        return set([0, num, num * 2])

      val = gen(i - 1)

      for el in [*val]:
        val.add(num + el)
        val.add(num * 2 + el)

      return val

    arr = sorted([*gen()])
    l = len(arr)
    val = baseCosts[0] - target

    for base in baseCosts:
      i = bisect_left(arr, target - base)

      for j in range(max(i - 1, 0), min(i + 1, l)):
        new = base + arr[j] - target

        if abs(new) < abs(val) or abs(new) == abs(val) and new < val:
          val = new

    return target + val