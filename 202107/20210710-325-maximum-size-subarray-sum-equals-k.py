class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """

    def maxSubArrayLen(self, nums, k):
        # Write your code here
        acc = [0]
        h = {0: 0}
        max_ = 0

        for (i, num) in enumerate(nums):
            val = num + acc[-1]
            acc.append(val)

            if val not in h:
                h[val] = i + 1

            last = val - k

            if last in h:
                max_ = max(max_, i + 1 - h[last])

        return max_
