class Solution:
  def minInsertions(self, s: str) -> int:
    N = len(s)
    stack = 0
    res = 0

    for i in range(0, N):
      if s[i] == '(':
        if stack & 1 == 1:
          res += 1
          stack += 1
        else:
          stack += 2
      else:
        if stack > 0:
          stack -= 1
        else:
          res += 1
          stack += 1

    return res + stack
