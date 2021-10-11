class Solution:
  def maxSizeSlices(self, slices: List[int]) -> int:
    m = len(slices) // 3

    def helper(sub):
      res = [[0] * (m + 1), [0] * (m + 1)]

      for s in sub:
        res.append([0] + [max(res[-2][i - 1] + s, res[-1][i])
                   for i in range(1, m + 1)])

      return max(tup[-1] for tup in res[-m:])

    return max(helper(slices[1:]), helper(slices[:-1]))