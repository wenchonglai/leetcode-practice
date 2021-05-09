class Solution:
  def maxJumps(self, arr: List[int], d: int) -> int:
    length = len(arr)
    h = {}

    def visit(i: int):
      if i in h:
        return

      h[i] = 1

      for j in range(i + 1, min(i + d + 1, length)):
        if arr[j] >= arr[i]:
          break

        if j not in h:
          visit(j)

        h[i] = max(h[i], h[j] + 1)

      for j in range(i - 1, max(-1, i - d - 1), -1):
        if arr[j] >= arr[i]:
          break

        h[i] = max(h[i], h[j] + 1)

    for (i, height) in enumerate(arr):
      visit(i)

    return max([h[i] for i in h])