class Solution:
    # 大致思路：最小子序列和的二分搜索
    # 子序列和不满 K 时将当前元素加入子序列和中，否则新开一个子序列
    # 注意：最后一个子序列和可能小于假定最小子序列和
    # 此时需要将最后子序列归并到前一个子序列，重新计算 max
    # （用数组或者双指针储存最近的两个子序列和）
    def maximizeSweetness(self, sweetness, K):
        # write your code here
        l = min(sweetness)
        r = sum(sweetness)
        maxmin = 0

        while l < r:
            m = (l + r) // 2
            arr = [0]

            for i in sweetness:
                if (arr[-1] < m):
                    arr[-1] += i
                else:
                    arr.append(i)

            if arr[-1] < m:
                last = arr.pop()
                arr[-1] += last

            length = len(arr)

            if length > K:
                l = m + 1
                maxmin = max(maxmin, min(arr))
            else:
                r = m
        
        return maxmin