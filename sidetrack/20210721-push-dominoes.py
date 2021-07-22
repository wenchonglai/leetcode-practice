class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    N = len(dominoes)
    seq = [None] * N
    s = [ch for ch in dominoes]
    
    ct = 0
    sign = None
    
    for i in range(N):
      ch = s[i]
      
      if ch == "R":
        ct = 1
        sign = ch
      elif ch == "L":
        ct = 1
        sign = None
      elif sign == "R":
        ct += 1
      
      if sign:
        seq[i] = ct
        s[i] = sign
        
    for i in range(N - 1, -1, -1):
      ch = s[i]
      
      if ch == "L":
        ct = 1
        sign = ch
      elif sign == "L":
        ct += 1
        
        if ch == 'R':
          if ct < seq[i]:
            s[i] = sign
          else:
            sign = None
            if ct == seq[i]:
              s[i] = "."
        else:
          seq[i] = ct
          s[i] = sign
      
    return ''.join(s)