# Rectangular Map of N x M, each tile has a shade(5 different shades total).
# A country:
#     Has tiles of the same shade
#     Can travel from one tile to another orthogonally(up down, left right) without another shade being in the way
# How many countries are there?

# Test Case: 11 countries here

from collections import defaultdict

def countCountries(dp):
  N = len(dp)
  M = len(dp[0])
  ct = 0
  visited = set()

  def traverse(tup):
    (x, y) = tup
    visited.add(tup)

    for (dx, dy) in ((-1, 0), (0, -1), (1, 0), (0, 1)):
      newX = x + dx
      newY = y + dy
      color = dp[y][x]
      
      if newX >= 0 and newX < M and newY >= 0 and newY < N:
        if dp[newY][newX] == color and (newX, newY) not in visited:
          traverse((newX, newY))
  
  for y in range(N):
    for x in range(M):
      if (x, y) not in visited:
        ct += 1
        traverse((x, y))
  
  return ct

print(
  countCountries(
    [[5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1]]
  )
)

