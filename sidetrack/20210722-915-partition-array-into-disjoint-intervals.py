class Solution:
  def partitionDisjoint(self, nums: List[int]) -> int:
    N = len(nums)
    sarr = sorted([(num, i) for (i, num) in enumerate(nums)])
    arr = [None] * N

    for (rank, (num, idx)) in enumerate(sarr):
      arr[idx] = rank

    m = None

    for (i, rank) in enumerate(arr):
      if not m or m < rank:
        m = rank

      if m <= i:
        return m + 1
