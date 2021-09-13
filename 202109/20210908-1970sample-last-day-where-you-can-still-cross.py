class Solution:
  def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
    grids = [[-1] * col for y in range(row)]
    N = len(cells)

    for (i, [y, x]) in enumerate(cells):
      grids[y - 1][x - 1] = i

    h = {}

    def dfs(x, y, day):
      nonlocal visited

      if 0 <= x < col and 0 <= y < row:
        if day > grids[y][x]:
          return False

        if y == 0:
          return day

        tup = (x, y)

        if tup in visited:
          return False

        visited.add(tup)

        for (dx, dy) in ((0, -1), (-1, 0), (1, 0), (0, 1)):
          tup_ = (x + dx, y + dy)

          if tup_ in h and h[tup_] >= day:
            return h[tup_]

          res = dfs(*tup_, day)

          if res != False:
            if tup_ not in h or h[tup_] < res:
              h[tup_] = res

            return res

      return False

    def ddfs(day):
      for x in range(col):
        y = row - 1

        if day <= grids[y][x]:

          if (x, y) in h and h[(x, y)] >= day:
            return True

          res = dfs(x, y, day)

          if res != False:
            if (x, y) not in h or h[(x, y)] < res:
              h[(x, y)] = res

            return True

    lo = 1
    hi = N - 1

    while lo < hi:
      mid = lo + hi + 1 >> 1
      visited = set()

      if ddfs(mid):
        lo = mid
      else:
        hi = mid - 1

    return hi
