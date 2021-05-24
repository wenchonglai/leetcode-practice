class Solution:
  def removeInvalidParentheses(self, s: str) -> List[str]:
    q = set([('', 0)])
    N = len(s)
    ct = 0
    max_len = 0

    for i in range(0, N):
      ch = s[i]

      if ch not in ['(', ')']:
        max_len += 1
        q = set([(sub + ch, ct) for (sub, ct) in q])
      elif ch == '(':
        ct += 1
        q = q.union([(sub + ch, ct + 1) for (sub, ct) in q])
      else:
        if ct > 0:
          ct -= 1
          max_len += 2

        q = q.union([(sub + ch, ct - 1) for (sub, ct) in q if ct > 0])

    return [_ for (_, ct) in q if ct == 0 and len(_) == max_len]