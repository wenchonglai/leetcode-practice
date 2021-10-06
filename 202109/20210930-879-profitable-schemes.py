class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        h = defaultdict(int)
        h[(0, 0)] = 1
        MOD = 10 ** 9 + 7

        for i in range(m):
          h1 = {}

          for (gAcc, pAcc) in h:
            if group[i] + gAcc > n:
              continue

            tup1 = (group[i] + gAcc, min(profit[i] + pAcc, minProfit))

            if tup1 not in h1:
              h1[tup1] = 0 if tup1 not in h else h[tup1]

            h1[tup1] += h[(gAcc, pAcc)]
            h1[tup1] %= MOD

          h |= {tup: h1[tup] for tup in h1}

        return sum(h[key] for key in h if key[1] >= minProfit) % MOD
