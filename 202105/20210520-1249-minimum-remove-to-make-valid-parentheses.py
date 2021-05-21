class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    N = len(s)
    ct = 0
    clear = set()

    for i in range(0, N):
      ch = s[i]
      if ch == '(':
        ct += 1
      elif ch == ')':
        if ct <= 0:
          clear.add(i)
        else:
          ct -= 1

    ct = 0

    for i in range(N - 1, -1, -1):
      ch = s[i]
      if ch == ')':
        ct += 1
      elif ch == '(':
        if ct <= 0:
          clear.add(i)
        else:
          ct -= 1

    res = ''
    start = 0

    for i in sorted(clear):
      res += s[start: i]
      start = i + 1

    res += s[start:]

    return res
