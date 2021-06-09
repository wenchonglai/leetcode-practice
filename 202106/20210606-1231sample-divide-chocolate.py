class Solution:
    """
    @param sweetness: an integer array
    @param K: an integer
    @return:  return the maximum total sweetness of the piece
    """

    def maximizeSweetness(self, sweetness, K):
        # write your code here
        total = sum(sweetness)
        l = 0
        r = total // K
        arr = sweetness
        max_ = 0

        while l < r:
            m = l + r >> 1
            ct = 0
            sum_ = 0
            next_ = None

            for (i, num) in enumerate(arr):
                sum_ += num

                if sum_ >= m:
                    ct += 1
                    sum_ = 0

            if ct > K:
                if max_ < m:
                    max_ = m

                l = m + 1
            else:
                r = m

        return max_