from collections import defaultdict

class Solution:
  def minJumps(self, arr: List[int]) -> int:
    v1 = set()
    v2 = set()
    h = defaultdict(set)
    q = [0]
    ct = 0
    last_i = len(arr) - 1
    
    for (i, num) in enumerate(arr):
      h[num].add(i)
    
    while q:
      q1 = []
      
      for i in q:
        num = arr[i]
        s = h[num]
        
        if i == last_i:
          return ct
        
        if i in v1 or i < 0 or i > last_i:
          continue
          
        if num not in v2:
          q1 += [*s]
          v2.add(num)
          
        if i not in v1:
          q1 += [i + 1, i - 1]
          v1.add(i)
    
      ct += 1
      q = q1