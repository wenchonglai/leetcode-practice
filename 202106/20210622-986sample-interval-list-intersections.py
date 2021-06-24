class Solution:
  def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    if not firstList or not secondList:
      return []

    i1, i2 = 0, 0
    l1, l2 = len(firstList), len(secondList)
    res = []

    while i1 < l1 and i2 < l2:
      f1, f2 = firstList[i1]
      s1, s2 = secondList[i2]

      if f2 < s1:
        i1 += 1
        continue

      if f1 > s2:
        i2 += 1
        continue

      if f2 <= s2:
        res.append([max(s1, f1), f2])
        i1 += 1

      else
        res.append([max(s1, f1), s2])
        i2 += 1

    return res
