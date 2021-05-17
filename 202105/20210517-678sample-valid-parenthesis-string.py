class Solution:
  def checkValidString(self, s: str) -> bool:
    #从左到右遍历，任一时刻 ( 和 * 数量大于 ) 时返回 False
    #从右到左遍历，任一时刻 ) 和 * 数量大于 ( 时返回 False
    #否则返回 True
    ct = 0
    N = len(s)

    for ch in s:
      if ch == '(' or ch == '*':
        ct += 1
      else:
        ct -= 1

      if ct < 0:
        return False

    ct = 0
    for ch in s[::-1]:
      if ch == ')' or ch == '*':
        ct += 1
      else:
        ct -= 1

      if ct < 0:
        return False

    return True
