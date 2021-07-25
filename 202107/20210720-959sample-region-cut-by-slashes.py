class Solution:
  def regionsBySlashes(self, grid: List[str]) -> int:
    h = {}
    N = len(grid)
    M = len(grid[0])
    visited = set()
    ct = 0
    
    def dfs(x, y, sub):
      if x not in range(M) or y not in range(N):
        return
      
      if (x, y, sub) in visited:
        return
      
      visited.add((x, y, sub))
      
      if sub == 0:
        dfs(x, y - 1, 2)
      elif sub == 1:
        dfs (x + 1, y, 3)
      elif sub == 2:
        dfs(x, y + 1, 0)
      elif sub == 3:
        dfs(x - 1, y, 1)
      
      if grid[y][x] != "\\":
        dfs(x, y, sub ^ 3)
      
      if grid[y][x] != "/":
        dfs(x, y, sub ^ 1)
    
    for y in range(N):
      for x in range(M):
        for sub in range(4):
          if (x, y, sub) not in visited:
            dfs(x, y, sub)
            ct += 1
    
    return ct