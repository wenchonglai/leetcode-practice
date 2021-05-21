import re

class Solution:
  def diffWaysToCompute(self, expression: str, strs={}) -> List[int]:
    # 遍历字符串中每一符号，递归得出符号左右子字符串不同的括号方式，其不同方式加总为结果
    if not re.search("[\+\-\*]", expression):
      return [int(expression)]

    N = len(expression)

    for i in range(0, N):
      ch = expression[i]

      if ch in '+-*':
        left = expression[0:i]
        right = expression[i + 1:]

        if left not in strs:
          strs[left] = self.diffWaysToCompute(left, strs)

        if right not in strs:
          strs[right] = self.diffWaysToCompute(right, strs)

        if expression not in strs:
          strs[expression] = []

        for n1 in strs[left]:
          for n2 in strs[right]:
            if ch == '+':
              strs[expression].append(n1 + n2)
            elif ch == '-':
              strs[expression].append(n1 - n2)
            else:
              strs[expression].append(n1 * n2)

    return strs[expression]
