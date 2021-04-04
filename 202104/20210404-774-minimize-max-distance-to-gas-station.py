class Solution:
    """
    @param stations: an integer array
    @param k: an integer
    @return: the smallest possible value of D
    """
    # 该题需要注意的是距离可以是无理数，因此不能简单地 l = m + 1，
    # 而是需要在循环条件中判断 l 和 r 的差值是否不大于最小容许差值

    def minmaxGasDist(self, stations, k):
        # Write your code here
        dists = [stations[i] - stations[i - 1]
                 for i in range(1, len(stations))]

        l = 1e-6
        r = max(dists)

        while l < r - 1e-6:
            m = (l + r) / 2.0
            count = 0

            for dist in dists:
                count += (dist / m) // 1

            if count > k:
                l = m
            else:
                r = m

        return l
