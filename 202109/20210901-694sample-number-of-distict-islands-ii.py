class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """

    def numberofDistinctIslands(self, grid):
        # 储存各岛屿的形状（以dfs的路径表示；数字表放方向，父子节点之间无间隔，兄弟节点之间用|间隔）
        # write your code here
        shapepath = None
        visited = set()
        s = set()
        m, n = len(grid[0]), len(grid)

        def dfs(x, y):
            nonlocal shapepath

            visited.add((x, y))

            for (i, (dx, dy)) in enumerate(((0, -1), (-1, 0), (1, 0), (0, 1))):
                x_, y_ = x + dx, y + dy
                if 0 <= x_ < m and 0 <= y_ < n and grid[y_][x_] == 1 and (x_, y_) not in visited:
                    shapepath += str(i)
                    dfs(x_, y_)
                shapepath += '|'

        for y in range(n):
            for x in range(m):
                if (x, y) not in visited and grid[y][x] == 1:
                    shapepath = ''
                    dfs(x, y)
                    s.add(shapepath)
                    shapepath = None

        if shapepath != None:
            s.add(shapepath)

        return len(s)
