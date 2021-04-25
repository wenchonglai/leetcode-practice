from sortedcontainers import SortedList
from collections import defaultdict

MOD = 10 ** 9 + 7

class Solution(object):
  def createSortedArray(self, instructions):
    """
    :type instructions: List[int]
    :rtype: int
    """
    arr = SortedList([])
    s = 0
    length = 0
    pos_hash = defaultdict(int)
    
    for num in instructions:
      l = arr.bisect_left(num)
      s += min(l, length - l - pos_hash[num])
      arr.add(num)
      pos_hash[num] += 1
      length += 1
    
    return s % MOD