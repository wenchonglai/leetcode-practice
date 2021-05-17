class Solution:
  def scoreOfParentheses(self, s: str) -> int:
    ct = 0
    stack = 0
    mode = True
    
    for ch in s:
      if ch == '(':
        stack += 1
        mode = True
      else:
        stack -= 1
        
        if mode:
          ct += 1 << stack
          mode = False
    
    return ct