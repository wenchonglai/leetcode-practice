# 超级慢的方法，用了 insort，复杂度O(N^2)
import bisect
from collections import defaultdict

class Solution:
  def oddEvenJumps(self, arr: List[int]) -> int:
    sortedArr = []
    lmHash = defaultdict(set)
    smHash = defaultdict(set)
    h = {}
    N = len(arr)

    for i in range(N - 1, -1, -1):
      num = arr[i]
      smIndex = bisect.bisect_left(sortedArr, num)
      lmIndex = smIndex if (
          smIndex < N - 1 - i and sortedArr[smIndex] == num) else smIndex - 1

      if smIndex < N - 1 - i and sortedArr[smIndex] in h:
        smHash[h[sortedArr[smIndex]]].add(i)

      if lmIndex >= 0 and sortedArr[lmIndex] in h:
        lmHash[h[sortedArr[lmIndex]]].add(i)

      h[num] = i
      bisect.insort(sortedArr, num)

    q1 = set([N - 1])
    q2 = set([N - 1])
    s = set([N - 1])

    while q1 or q2:
      q1, q2 = set().union(*[lmHash[i] for i in q2]
                           ), set().union(*[smHash[i] for i in q1])
      s = s.union(q2)

    return len(s)