class Solution:
  def canReach(self, arr: List[int], start: int) -> bool:
    visited = set()
    q = [start]
    length = len(arr)
    
    while q:
      pos = q.pop()
      
      if arr[pos] == 0:
        return True
      
      visited.add(pos)
      
      l = pos - arr[pos]
      r = pos + arr[pos]
      
      if l >= 0 and not l in visited:
        q.append(l)
      
      if r < length and not r in visited:
        q.append(r)
      
    return False
    
    
    