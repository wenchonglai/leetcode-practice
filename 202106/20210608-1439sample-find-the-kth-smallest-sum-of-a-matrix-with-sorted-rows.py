from heapq import *


class Solution:
  def kthSmallest(self, mat: List[List[int]], k: int) -> int:
    N = len(mat)
    M = len(mat[0])
    sum_ = sum(sub[0] for sub in mat)
    posArr0 = [0] * N
    h = [(sum_, posArr0, 0)] #第二个元素是每列的索引；第一个元素是各列在索引处的数字和；第三个元素是最小的可右移的索引，目的是允许 (1, 0) -> (1, 1)，但防止 (0, 1) -> (1, 1)

    #进行 k - 1 次操作，每次最小元素出堆；遍历各行，依次将最小元素所拥有的各行索引右移 1，并将新的和、索引序列、最小可移动索引的行数进堆
    #假设某次移动了第 i 行的索引，则其后不得再移动第i行以前的索引；否则，若移动第 i 行后再移动第 i - k 行的行为，将与移动第 i - k 行后再移动第 i 行的行为重复
    for i in range(k - 1):
      s_, posArr, curr = heappop(h)

      for j in range(curr, N):
        posJ = posArr[j]

        if posJ == M - 1:
          continue

        s1 = s_ + mat[j][posJ + 1] - mat[j][posJ]
        posArr1 = list(posArr)
        posArr1[j] = posJ + 1
        heappush(h, (s1, posArr1, j))

    return heappop(h)[0]
