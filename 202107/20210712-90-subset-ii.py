class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    N = len(nums)
    visited = set([()])
    
    for num in nums:
      for tup in [*visited]:
        newTup = tuple([*tup, num])
        
        if newTup not in visited:
          visited.add(newTup)
          
    return [list(tup) for tup in visited]