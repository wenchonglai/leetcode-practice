class UF:
  def __init__(self):
    self.parents = {}

  def find(self, i):
    if i not in self.parents:
      self.parents[i] = i
    elif self.parents[i] != i:
      self.parents[i] = self.find(self.parents[i])

    return self.parents[i]

  def union(self, a, b):
    aRoot, bRoot = self.find(a), self.find(b)

    if aRoot == bRoot:
      return

    if aRoot > bRoot:
      bRoot, aRoot = aRoot, bRoot

    self.parents[bRoot] = aRoot


class Solution:
  def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
    uf = UF()

    @cache
    def isEq(a, b):
      return uf.find(a) == uf.find(b)

    primeArr = [True] * (n + 1)

    for num in range(threshold + 1, n + 1):
      if primeArr[num] == True:
        for mul in range(num, n + 1, num):
          if num != mul:
            primeArr[mul] = False
          # 注意不要加 if mul in pool 条件。这题从 0 - n 的城市都存在
          uf.union(mul, num)

    return [isEq(a, b) for [a, b] in queries]
