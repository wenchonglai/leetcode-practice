class Solution:
  def shortestBridge(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    edges = []

    def fill2(x, y):
      if 0 <= x < m and 0 <= y < n and grid[y][x] == 1:
        grid[y][x] = 2
        fill2(x - 1, y)
        fill2(x + 1, y)
        fill2(x, y - 1)
        fill2(x, y + 1)

    def findEdges(x, y):
      nonlocal edges

      if 0 <= x < m and 0 <= y < n:
        if grid[y][x] == 0:
          edges.append((x, y))
          grid[y][x] = 4

        if grid[y][x] == 2:
          grid[y][x] = 3
          findEdges(x - 1, y)
          findEdges(x + 1, y)
          findEdges(x, y - 1)
          findEdges(x, y + 1)

    found = False

    for y in range(n):
      for x in range(m):
        if grid[y][x] == 1:
          fill2(x, y)
          found = True
          break

      if found == True:
        break

    findEdges(x, y)
    ct = 0

    while edges:
      _edges = []
      ct += 1

      for (x, y) in edges:
        for (dx, dy) in ((-1, 0), (1, 0), (0, 1), (0, -1)):
          x_, y_ = x + dx, y + dy
          if 0 <= x_ < m and 0 <= y_ < n:
            if grid[y_][x_] == 1:
              return ct

            elif grid[y_][x_] == 0:
              _edges.append((x_, y_))
              grid[y_][x_] = 4

      edges = _edges
