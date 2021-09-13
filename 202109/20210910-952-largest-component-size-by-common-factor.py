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
    elif aRoot > bRoot:
      bRoot, aRoot = aRoot, bRoot

    self.parents[bRoot] = aRoot


class Solution:
  def largestComponentSize(self, nums: List[int]) -> int:
    max_ = max(nums)
    arr = [True] * (max_ + 1)
    pool = set(nums)
    uf = UF()

    for num in range(2, max_ + 1):
      if arr[num] == True:
        for div in range(num, max_ + 1, num):
          if div != num:
            arr[num] = False

          if div in pool:
            uf.union(div, num)

    h = defaultdict(int)

    for num in nums:
      h[uf.find(num)] += 1

    return max(h[key] for key in h)
