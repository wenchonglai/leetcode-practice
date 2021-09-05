# LintCode 434 · Number of Islands II

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, m, n, operators):
        # write your code here
        res = []
        grid = {}
        ct = 0

        def findroot(x, y):
            nonlocal grid

            while (x, y) != grid[(x, y)]:
                (x, y) = grid[(x, y)]

            return (x, y)

        for op in operators:
            x, y = op.x, op.y

            for (dx, dy) in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                x_, y_ = x + dx, y + dy

                if 0 <= x_ < m and 0 <= y_ < n and (x_, y_) in grid:
                    tup = findroot(x_, y_)

                    if (x, y) not in grid:
                        grid[(x, y)] = tup
                    else:
                        t2 = findroot(x, y)

                        if grid[tup] != t2:
                            grid[(x_, y_)] = t2
                            grid[tup] = t2
                            ct -= 1

            if (x, y) not in grid:
                grid[(x, y)] = (x, y)
                ct += 1

            res.append(ct)

        return res
