class Solution:
  def canJump(self, nums: List[int]) -> bool:
    l = len(nums)
    m = 0

    for (i, num) in enumerate(nums):
      if m < i:
        continue
        
      if i + num >= l - 1:
        return True 
    
      if i + num > m:
        m = i + num
    
    return False