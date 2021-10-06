class Solution:
  def largestNumber(self, cost: List[int], target: int) -> str:
    slots = [0] + [-1] * target

    tups = sorted((c, i + 1) for (i, c) in enumerate(cost))

    for t in range(1, target + 1):
      for (c, digit) in tups:
        if t - c >= 0 and slots[t - c] >= 0:
          slots[t] = max(slots[t], slots[t - c] * 10 + digit)

    val = slots[-1]
    return str(val) if val > 0 else "0"
