from collections import defaultdict, deque

class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    nums = sorted(nums)
    h = defaultdict(int)
    arr = deque([0, 0])

    for num in nums:
      h[num] += 1

    keys = [key for key in h]

    for (i, key) in enumerate(keys):
      if i == 0 or key > keys[i - 1] + 1:
        arr.append(max(arr[-2], arr[-1]) + h[key] * key)
      else:
        arr.append(max(arr[-2] + h[key] * key, arr[-1]))

    return max(arr)
