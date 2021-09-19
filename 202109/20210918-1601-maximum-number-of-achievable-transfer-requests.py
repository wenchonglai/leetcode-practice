class Solution:
  def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
    arr = [0] * n
    res = 0
    m = len(requests)

    def dfs(i, curr):
      nonlocal res

      if i == m:
        for num in arr:
          if num != 0:
            return

        if curr > res:
          res = curr

        return

      [fromI, toI] = requests[i]

      dfs(i + 1, curr)

      arr[fromI] -= 1
      arr[toI] += 1

      dfs(i + 1, curr + 1)

      arr[fromI] += 1
      arr[toI] -= 1

    dfs(0, 0)
    return res