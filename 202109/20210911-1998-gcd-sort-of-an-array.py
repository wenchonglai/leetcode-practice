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
    aRoot = self.find(a)
    bRoot = self.find(b)

    if aRoot == bRoot:
      return
    elif aRoot > bRoot:
      bRoot, aRoot = aRoot, bRoot

    self.parents[bRoot] = aRoot


class Solution:
  def gcdSort(self, nums: List[int]) -> bool:
    sarr = sorted(nums)
    n = len(nums)
    uf = UF()
    max_ = sarr[-1]
    arr = [True] * (max_ + 1)
    pool = set(nums)

    for num in range(2, max_ + 1):
      if arr[num]:
        for div in range(num, max_ + 1, num):
          if num != div:
            arr[div] = False

          if div in pool:
            uf.union(num, div)

    bol = True

    for i in range(n):
      if uf.find(sarr[i]) != uf.find(nums[i]):
        return False

    return True
