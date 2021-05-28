class Solution:
  def countTriplets(self, arr: List[int]) -> int:
    N = len(arr)
    s = 0

    for i in range(0, N):
      val = 0

      for j in range(i, N):
        val ^= arr[j]

        if val == 0:
          s += j - i

    return s
