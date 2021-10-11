class Solution:
    def minCostII(self, costs):
        n = len(costs)
        k = len(costs[0]) if n != 0 else 0

        if n == 0 or k == 0:
            return 0

        dp = [[0] * k for i in range(n)]
        m1, m2 = 0, 0

        for i in range(n):
            t1, t2 = None, None

            for j in range(k):
                cost = costs[i][j]
                last = dp[i - 1][j] if i > 0 else 0
                res = cost + (m1 if last != m1 else m2)

                if t1 == None or res < t1:
                    t1, t2 = res, t1
                elif t2 == None or res < t2:
                    t2 = res

                dp[i][j] = res

            if t2 == None:
                t2 = t1

            m1, m2 = t1, t2
            
        return min(dp[-1])
