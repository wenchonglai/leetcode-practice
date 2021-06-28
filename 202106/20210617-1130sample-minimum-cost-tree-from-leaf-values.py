class Solution:
  def mctFromLeafValues(self, arr: List[int]) -> int:
    # 思路：假设 arr[i] * arr[i + 1] 乘积最小，则取出 arr[i] 和 arr[i + 1] 中较小的一个，并把乘积加到返回值中。直到 arr 被抽到剩下一个数

    res = 0
    length = len(arr)

    while length > 1:
      idx = min([i for i in range(0, length - 1)],
                key=lambda i: arr[i] * arr[i + 1])
      res += arr[idx] * arr[idx + 1]
      arr[idx] = max(arr[idx], arr[idx + 1])
      arr.pop(idx + 1)

      length -= 1

    return res
