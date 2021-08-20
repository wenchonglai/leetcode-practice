class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """

    def wiggleSort(self, nums):
        N = len(nums)

        if N <= 1:
            return nums

        for i in range(N // 2):
            if nums[i * 2] > nums[i * 2 + 1]:
                nums[i * 2], nums[i * 2 + 1] = nums[i * 2 + 1], nums[i * 2]

            if nums[i * 2] > nums[i * 2 - 1]:
                nums[i * 2 - 1], nums[i * 2] = nums[i * 2], nums[i * 2 - 1]

        if N % 2 == 1 and nums[-1] > nums[-2]:
            nums[-2], nums[-1] = nums[-1], nums[-2]
