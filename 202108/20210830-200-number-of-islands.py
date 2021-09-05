class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    N = len(grid)
    M = len(grid[0])
    ct = 0

    def dfs(x, y):
      grid[y][x] = ''

      for (dx, dy) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        x_ = x + dx
        y_ = y + dy

        if x_ >= 0 and x_ < M and y_ >= 0 and y_ < N and grid[y_][x_] == "1":
          dfs(x_, y_)

    for x in range(M):
      for y in range(N):
        if grid[y][x] == "1":
          dfs(x, y)
          ct += 1

    return ct
