class Solution:
  def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
    s1 = 0
    s2 = 0
    s = 0
    mod = 10 ** 9 + 7

    while nums1 and nums2:
      res = nums1[-1] - nums2[-1]

      if res > 0:
        s1 += nums1.pop()
      elif res < 0:
        s2 += nums2.pop()
      else:
        s += max(s1, s2) % mod
        s1 = nums1.pop()
        s2 = nums2.pop()

    return (s + max(s1 + sum(nums1), s2 + sum(nums2))) % mod
