class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    def getCount(val):
      acc = 0
      ct = 1

      for i in range(1, N):
        acc += s_pos[i] - s_pos[i - 1]

        if acc >= val:
          acc = 0
          ct += 1

      return ct

    N = len(position)
    s_pos = sorted(position)

    l = 1
    r = (s_pos[-1] - s_pos[0]) // (m - 1) + 1

    while l < r:
      mid = l + r + 1 >> 1

      if getCount(mid) < m:
        r = mid - 1
      else:
        l = mid

    return l
