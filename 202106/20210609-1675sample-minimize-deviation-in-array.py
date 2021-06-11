from heapq import *
# 优先队列

class Solution:
  def minimumDeviation(self, nums: List[int]) -> int:
    hi = max(nums) #只取最大值而不排序，复杂度O(N)
    heapify(nums)  #构造最小堆，取最小值
    lo = nums[0]
    res = hi - lo  #初始的最小差值为 hi - lo

    #最小值为奇数时，反复弹出最小值，x2，再压入堆中，更新最小值、最大值、最小差值
    while lo % 2 == 1:
      heapreplace(nums, lo * 2)
      hi = max(hi, lo * 2)
      lo = nums[0]
      res = min(res, hi - lo)

    #构造最大堆
    nums = [-num for num in nums]
    heapify(nums)

    #最大值为偶数时，反复弹出最小值，/2，再压入堆中，更新最小值、最大值、最小差值
    while hi % 2 == 0:
      heapreplace(nums, -hi // 2)
      lo = min(hi // 2, lo)
      hi = -nums[0]
      res = min(res, hi - lo)

    return res
