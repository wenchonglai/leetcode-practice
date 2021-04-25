from sortedcontainers import SortedList

class Solution(object):
  def reversePairs(self, nums):
    rank = SortedList([])
    ct = 0
    s = 0

    for num in nums:
      i = rank.bisect_left(num * 2 + 1)
      s += ct - i
      ct += 1
      rank.add(num)

    return s