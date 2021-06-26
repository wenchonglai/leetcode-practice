from collections import defaultdict

class Solution:
  def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    def helper(nums1, nums2):
      h = defaultdict(int)

      for num in nums1:
        h[num ** 2] += 1

      return sum([h[num * nums2[j]] for (i, num) in enumerate(nums2) for j in range(i) if num * nums2[j] in h])

    return helper(nums1, nums2) + helper(nums2, nums1)
