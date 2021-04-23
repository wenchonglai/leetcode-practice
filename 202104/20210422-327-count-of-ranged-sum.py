from sortedcontainers import SortedList

class Solution(object):
  def countRangeSum(self, nums, lower, upper):
    rank = SortedList([0])
    res = 0
    sum = 0
    
    for num in nums:
      sum += num
      left = rank.bisect_left(sum - upper)
      right = rank.bisect_right(sum - lower)
      if right > left:
        res += right - left
        
      rank.add(sum)
      
    return res