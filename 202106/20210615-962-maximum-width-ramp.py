class Solution:
  def maxWidthRamp(self, nums: List[int]) -> int:
    N = len(nums)
    curr = max(nums)
    h = {curr: 0}
    _max = 0
    
    for i in range(0, N):
      num = nums[i]
      
      while curr >= num:
        h[curr] = i
        curr -= 1
    
      if num in h and i - h[num] > _max:
        _max = i - h[num]
        
    return _max
      