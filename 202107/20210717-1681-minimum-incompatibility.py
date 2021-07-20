class Solution:
  def minimumIncompatibility(self, nums: List[int], k: int) -> int:
    N = len(nums)
    nums = sorted(nums)
    M = N // k

    if M == 1:
      return 0

    @cache
    def getMin(tup, tup2):
      if not tup2:
        return nums[tup[-1]] - nums[tup[0]]

      if len(tup) == M:
        v1 = getMin(tup, None)
        v2 = getMin(tuple([tup2[0]]), tuple(list(tup2)[1:]))
        return v1 + v2 if v1 and v2 else None

      min_ = None
      l = list(tup)
      l2 = list(tup2)

      for (i, idx) in enumerate(l2):
        if not l or nums[l[-1]] < nums[idx]:
          val = getMin(tuple(l + [idx]), tuple(l2[:i] + l2[i + 1:]))

          if not min_ or val and min_ > val:
            min_ = val

      return min_

    val = getMin(tuple([0]), tuple([i for i in range(1, N)]))

    return val if val else -1
