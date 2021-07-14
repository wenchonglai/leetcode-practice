class Solution:
  def numSquarefulPerms(self, nums: List[int]) -> int:
    N = len(nums)
    visited = set()

    @cache
    def helper(tup1, tup2):
      l = list(tup2)

      if len(tup1) > 1:
        prod = tup1[-2] + tup1[-1]
        sqrt = int(prod ** 0.5)

        if sqrt ** 2 != prod:
          return

        if len(l) == 0:
          visited.add(tup1)

      for (i, num) in enumerate(l):
        helper(tuple([*tup1, num]), tuple(l[:i] + l[i + 1:]))

    helper(tuple(), tuple(nums))
    return len(visited)
