class Solution:
  def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
    cache1 = 0
    cache2 = 0
    i1 = 0
    i2 = 0
    N1 = len(nums1)
    N2 = len(nums2)
    res = 0
    MOD = 10 ** 9 + 7

    while i1 < N1 and i2 < N2:
      if nums1[i1] < nums2[i2]:
        cache1 += nums1[i1]
        i1 += 1
      elif nums1[i1] > nums2[i2]:
        cache2 += nums2[i2]
        i2 += 1
      else:
        res += nums1[i1] + max(cache1, cache2)
        cache1 = cache2 = 0
        i1 += 1
        i2 += 1

    return (res + max(cache1 + sum(nums1[i1:]), cache2 + sum(nums2[i2:]))) % MOD
