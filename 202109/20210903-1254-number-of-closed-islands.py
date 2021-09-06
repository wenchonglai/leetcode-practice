class Solution:
  def closedIsland(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    def fill(x, y):
      if 0 <= x < m and 0 <= y < n and grid[y][x] == 0:
        grid[y][x] = 1
        fill(x - 1, y)
        fill(x + 1, y)
        fill(x, y - 1)
        fill(x, y + 1)

    for x in range(0, m):
      fill(x, 0)
      fill(x, n - 1)

    for y in range(1, n - 1):
      fill(0, y)
      fill(m - 1, y)

    ct = 0

    for x in range(0, m):
      for y in range(0, n):
        if grid[y][x] == 0:
          fill(x, y)
          ct += 1

    return ct
