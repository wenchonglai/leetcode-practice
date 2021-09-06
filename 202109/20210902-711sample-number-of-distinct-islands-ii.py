class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """

    def numDistinctIslands2(self, grid):
        # write your code here
        # 把每个形状的保持不变、旋转、翻转后的形状相对最小顶点的x,y以str的形式储存
        # 旋转 = 水平/垂直翻转 + 沿对角线翻转
        n, m = len(grid), len(grid[0])

        def cardinal(pts):
            arr = []

            def stringify(pts):
                sarr = sorted(pts)
                (x0, y0) = sarr[0]

                return ';'.join([str(x - x0) + ',' + str(y - y0) for (x, y) in sarr])

            for (i, j) in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                arr.append(stringify([(x * i, y * j) for (x, y) in pts]))
                arr.append(stringify([(y * j, x * i) for (x, y) in pts]))

            return min(arr)

        def dfs(x, y):
            nonlocal m
            nonlocal n
            nonlocal pts

            if 0 <= x < m and 0 <= y < n and grid[y][x] == 1:
                grid[y][x] = 0
                pts.append((x, y))
                dfs(x, y - 1)
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y + 1)

        res = set()

        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    pts = []
                    dfs(x, y)
                    res.add(cardinal(pts))
        print(res)
        return len(res)
