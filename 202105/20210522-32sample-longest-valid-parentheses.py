class Solution:
  def longestValidParentheses(self, s: str) -> int:
    N = len(s)
    m = 0
    stack = []

    for i in range(0, N):
      ch = s[i]

      if ch == '(':
        stack.append(i)
      else:
        if stack and s[stack[-1]] == '(':
          stack.pop()
        else:
          stack.append(i)

        m = max(m, i - (stack[-1] if stack else -1))

    return m
