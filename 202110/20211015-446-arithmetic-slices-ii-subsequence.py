class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for i in range(len(nums))]
        res = 0

        for i in range(1, len(nums)):
          for j in range(i):
            delta = nums[i] - nums[j]
            val = dp[j][delta]
            dp[i][delta] += val + 1
            res += val

        return res
