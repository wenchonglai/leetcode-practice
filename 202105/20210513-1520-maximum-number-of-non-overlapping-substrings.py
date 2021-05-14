class Solution:
  def maxNumOfSubstrings(self, s: str) -> List[str]:
    # 每次出栈时，栈末字符的最后出现位置更新为出栈字符和栈末字符最后出现位置中较后的那一个
    def pop():
      popped = stack.pop()

      if stack and stack[-1][0] < popped[0]:
        stack[-1][1] = max(stack[-1][1], popped[1])

      return popped

    N = len(s)
    first = {}
    last = {}

    # 注册字符首次和最后一次出现的位置
    for (i, ch) in enumerate(s):
      last[ch] = i

      if ch not in first:
        first[ch] = i

    stack = []
    res = []

    for (i, ch) in enumerate(s):
      # 若字符第一次出现，则进栈
      if i == first[ch]:
        stack.append([first[ch], last[ch]])

      # 若字符最后一次出现，则将所有包含该字符的其它字符（第一次出现于该字符第一次之前）出栈
      # 并用 pop 更新这些字符的最末出现位置
      if i == last[ch] and stack and i == stack[-1][1]:
        popped = pop()
        res.append(s[popped[0]:popped[1] + 1])

        while stack and stack[-1][0] < popped[0]:
          pop()

      while stack and first[ch] < stack[-1][0]:
        pop()

    # 若某字符 ch 首次出现于 i0，现在又出现于 i，则：
    # i0 至 i 之间出现过，而且并非最后一次出现的所有字符都必须包含字符 ch；
    # 因此无需考虑这些字符（出栈），只需将字符 ch 出现的右边界移动到这些字符的最右右边界处
    return res if res else [s]
