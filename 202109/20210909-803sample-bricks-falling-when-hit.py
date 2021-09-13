# UF 储存 rank 和 size；最后加一格作为所有顶边格的根
# 初始化时克隆 grid 数组，然后把被敲的格子都去掉，遍历计算 UF 关系
# 然后倒序遍历 hits 数组，每次把当前的 hit 放回 grid 数组的克隆里，然后遍历 hit 格的邻边，重新进行 union，然后计算重新 union 后连结到顶边的格子个数
class UF:
  def __init__(self, size):
    self.size = size + 1
    self.parents = [*range(size + 1)]
    self.ranks = [0] * (size + 1)
    self.sizes = [1] * (size + 1)

  def findRoot(self, i):
    if i != self.parents[i]:
      self.parents[i] = self.findRoot(self.parents[i])

    return self.parents[i]

  def union(self, a, b):
    aRoot, bRoot = self.findRoot(a), self.findRoot(b)
    aRank, bRank = self.ranks[aRoot], self.ranks[bRoot]

    if aRoot == bRoot:
      return

    if aRank == bRank:
      self.ranks[aRoot] += 1
    elif aRank < bRank:
      bRoot, aRoot = aRoot, bRoot

    self.parents[bRoot] = aRoot
    self.sizes[aRoot] += self.sizes[bRoot]

  def getRootSize(self, i):
    return self.sizes[self.findRoot(i)]

  def getTopSize(self):
    return self.getRootSize(self.size - 1) - 1

class Solution:
  def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    n, m = len(grid), len(grid[0])
    size = m * n

    def idx(x, y):
      return y * m + x

    def adj(x, y):
      for (dx, dy) in ((0, -1), (-1, 0), (1, 0), (0, 1)):
        x_, y_ = x + dx, y + dy

        if 0 <= x_ < m and 0 <= y_ < n:
          yield x_, y_

    gridDup = [sub[:] for sub in grid]

    for (y, x) in hits:
      gridDup[y][x] = 0

    uf = UF(m * n)

    for y in range(n):
      for x in range(m):
        if gridDup[y][x] == 1:
          i = idx(x, y)

          if y == 0:
            uf.union(i, size)
          if x > 0 and gridDup[y][x - 1] == 1:
            uf.union(i, idx(x - 1, y))
          if y > 0 and gridDup[y - 1][x] == 1:
            uf.union(i, idx(x, y - 1))

    res = []

    for (y, x) in hits[::-1]:
      if grid[y][x] == 0:
        res.append(0)
      else:
        preTopSize = uf.getTopSize()
        i = idx(x, y)

        for x_, y_ in adj(x, y):
          if gridDup[y_][x_] == 1:
            uf.union(i, idx(x_, y_))

        if y == 0:
          uf.union(i, size)

        gridDup[y][x] = 1
        res.append(max(0, uf.getTopSize() - preTopSize - 1))

    return res[::-1]
