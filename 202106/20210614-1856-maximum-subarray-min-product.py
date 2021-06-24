class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
      N = len(nums)
      MOD = 10 ** 9 + 7
      xs = [0] * (N + 1)
      arr = [None] * (N + 1)
      stack = []
      arr[0] = 0
      _max = 0

      for i in range(N):
        xs[i + 1] = xs[i] + nums[i]

      for i in range(N):
        num = nums[i]

        while stack and nums[stack[-1]] >= nums[i]:
          stack.pop()

        arr[i] = stack[-1] + 1 if stack else 0
        stack.append(i)

      stack = []

      for i in range(N - 1, -1, -1):
        num = nums[i]

        while stack and nums[stack[-1]] >= nums[i]:
          stack.pop()

        right = stack[-1] if stack else N
        temp = (xs[right] - xs[arr[i]]) * nums[i]

        if temp > _max:
            _max = temp

        stack.append(i)

      return _max % MOD