class Solution:
  def maxProfit(self, inventory: List[int], orders: int) -> int:
    h = {}
    arr = []

    for num in sorted(inventory, reverse=True):
      if num not in h:
        h[num] = 1
        arr.append(num)
      else:
        h[num] += 1

    s = 0
    ct = 0
    i = 0
    MOD = 10 ** 9 + 7
    N = len(arr)

    while orders > 0:
      num = arr[i]
      h_num = h[num]
      deltaCt = orders - ct

      if i + 1 < N:
        num1 = arr[i + 1]
        maxDeltaCt = h_num * (num - num1)
        maxDeltaSum = maxDeltaCt * (num + num1 + 1) // 2

        if maxDeltaCt < deltaCt:
          s += maxDeltaSum
          ct += maxDeltaCt
          h[num1] += h_num
          i += 1
          s %= MOD
        else:
          times = deltaCt // h_num
          lastTime = deltaCt % h_num
          return (s + h_num * (num * 2 - times + 1) * times // 2 + lastTime * (num - times)) % MOD
      else:
        times = deltaCt // h_num
        lastTime = deltaCt % h_num
        return (s + h_num * (num * 2 - times + 1) * times // 2 + lastTime * (num - times)) % MOD
