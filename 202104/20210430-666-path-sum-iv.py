from collections import defaultdict

class Solution:
    def pathSum(self, nums):
        # write your code here
        h = defaultdict(int)
        h2 = defaultdict(bool)
        s = 0

        for num in nums:
            key = num // 10
            depth = key // 10
            i = key % 10

            h[key] = num % 10
            h2[depth * 10 - 10 + (i + 1) // 2] = True

        for num in nums:
            key = num // 10
            depth = key // 10
            i = key % 10

            if not h2[key]:
                while depth > 0:
                    s += h[depth * 10 + i]
                    depth -= 1
                    i = (i + 1) // 2

        return s
