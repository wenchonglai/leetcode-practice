class Solution:
  def hIndex(self, citations: List[int]) -> int:
    l = 0
    r = len(citations) - 1
    acc = 0

    while l <= r:
      m = (l + r + 1) // 2
      acc += r - m + 1
      cm = citations[m]

      if cm == acc:
        return acc

      if l == r:
        return acc if cm > acc else acc - 1

      if cm < acc:
        acc -= r - m + 1
        l = m

      else:
        r = m - 1

    return acc
