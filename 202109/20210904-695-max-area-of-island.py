class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    ct = 0
    maxCt = 0
    n, m = len(grid), len(grid[0])

    def dfs(x, y):
      nonlocal ct

      if 0 <= x < m and 0 <= y < n and grid[y][x] == 1:
        ct += 1
        grid[y][x] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    for x in range(0, m):
      for y in range(0, n):
        if grid[y][x] == 1:
          ct = 0
          dfs(x, y)
          maxCt = max(ct, maxCt)

    return maxCt
