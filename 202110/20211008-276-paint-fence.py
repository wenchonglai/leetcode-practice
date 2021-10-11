class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        # write your code here
        n = len(costs)

        if n == 0:
            return 0

        dp = [[None] * 3 for i in range(n)]
        dp[0] = [*costs[0]]

        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1]
                               [j - 2]) + costs[i][j]

        return min(dp[-1])
