class Solution:
  def longestWPI(self, hours: List[int]) -> int:
    h = {}
    N = len(hours)
    arr = [None] * N
    arr[0] = 1 if hours[0] > 8 else -1
    h[arr[0]] = 0
    _max = 1 if arr[0] == 1 else 0
    
    for i in range(1, N):
      arr[i] = arr[i - 1] + (1 if hours[i] > 8 else -1)
      num = arr[i]
      
      if num not in h:
        h[num] = i 
        
      if num > 0:
        _max = max(_max, i + 1)
      elif num - 1 in h:
        _max = max(_max, i - h[num - 1])

    return _max
      