class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    h = {}

    for num in nums:
      if num not in h:
        h[num] = 0
      h[num] += 1

    keys = sorted(h.keys())
    lk = len(keys)
    arr = [0, 0]
    res = 0

    for (i, k) in enumerate(keys):
      arr.append(max(arr[-2] + k * h[k], arr[-1]))
      if i < lk - 1 and keys[i + 1] > k + 1:
        res += max(arr[-2:])
        arr = [0, 0]

    res += max(arr[-2:])

    return res