from collections import defaultdict


class Solution:
  def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    h1 = defaultdict(int)
    h2 = defaultdict(int)
    s = 0
    ct = 0

    for num in nums1:
      s += num
      h1[num] += 1

    for num in nums2:
      s -= num
      h2[num] += 1

    if s < 0:
      h1, h2, s = h2, h1, -s

    for i in range(6):
      unit = 5 - i
      n1 = h1[6 - i]
      n2 = h2[i + 1]

      if s <= (n1 + n2) * unit:
        ct += (s + unit - 1) // unit
        return ct

      ct += n1 + n2
      s -= (n1 + n2) * unit

    return -1
