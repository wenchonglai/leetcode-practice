class Solution:
  def minFlips(self, mat: List[List[int]]) -> int:
    n, m = len(mat), len(mat[0])
    size = m * n
    biArr = []
    res = 10

    def idx(x, y):
      return x + y * m

    def toBi(x, y):
      bi = 1 << idx(x, y)

      for (dx, dy) in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        x_, y_ = x + dx, y + dy

        if 0 <= x_ < m and 0 <= y_ < n:
          bi |= 1 << idx(x_, y_)

      return bi

    val = 0

    for y in range(n):
      for x in range(m):
        biArr.append(toBi(x, y))
        if mat[y][x] == 1:
          val |= 1 << idx(x, y)

    @cache
    def dfs(curr, i, ct):
      nonlocal res

      if curr == 0:
        res = min(res, ct)

      if i == size:
        return

      for j in range(i, size):
        dfs(curr ^ biArr[j], j + 1, ct + 1)

    dfs(val, 0, 0)
    return -1 if res == 10 else res
