from heapq import *


class Solution:
    """
    @param A: a list of integer
    @param B: an integer
    @return: return a list of integer
    """

    def cheapestJump(self, a, b):
        # write your code here
        a = [0] + a
        n = len(a)
        h = {1: 0}
        dp = [None] * (n)
        dp[0] = (0, 0)
        dp[1] = None if a[1] == -1 else (a[1], 1)

        for (i, cost) in enumerate(a):
            if i == 0 or cost == -1:
                continue

            for j in range(max(1, i - b), i):
                if dp[j] != None:
                    (cj, lj) = dp[j]

                    if dp[i] != None:
                        (ci, li) = dp[i]

                        if ci < cj + cost or ci == cj + cost and li > lj:
                            continue

                    dp[i] = (cj + cost, lj + 1)
                    h[i] = j

        res = [n - 1]

        while res[-1] in h:
            res.append(h[res[-1]])

        return res[::-1][1:] if res[-1] == 0 else []
