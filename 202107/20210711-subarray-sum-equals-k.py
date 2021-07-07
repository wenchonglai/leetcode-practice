class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    h = {0: 1}
    acc = [0]
    res = 0

    for (i, num) in enumerate(nums):
      val = acc[-1] + num
      acc.append(val)

      if val not in h:
        h[val] = 1
      else:
        h[val] += 1

      if val - k in h:
        res += h[val - k]

        if k == 0:
          res -= 1

    return res
