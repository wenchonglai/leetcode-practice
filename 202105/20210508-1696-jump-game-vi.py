import heapq

class Solution:
  def maxResult(self, nums: List[int], k: int) -> int:
    hq = []
    h = {}

    for (i, num) in enumerate(nums):
      if hq:
        while h[hq[0]] < i - k:
          heapq.heappop(hq)

      val = hq[0] - num if hq else -num
      h[val] = i
      heapq.heappush(hq, val)

    if hq:
      while h[hq[0]] < i:
        heapq.heappop(hq)

    return -hq[0] if hq else 0
