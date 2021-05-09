class Solution:
  def oddEvenJumps(self, arr: List[int]) -> int:
    N = len(arr)

    def make(_arr):
      # 对所以元素求每个之后大于本元素的最大最小值或最小最大值；复杂度 O(N)
      # 解法：对元素的 index 按元素值大小排序；遍历排序数列，每次遍历到的 index 进栈
      # 进栈前判断当前 index 是否大于栈尾的 index元素（否则，当前 index 出于栈尾 index 之前，与求元素之后的最大最小/最小最大值矛盾），
      # 若是，则栈尾 index 指向当前 index
      stack = []
      _a = [None] * N

      for i in _arr:
        while stack and i > stack[-1]:
          _a[stack.pop()] = i
        stack.append(i)

      return _a

    a1 = make(sorted(range(0, N), key=lambda i: arr[i]))  # next smallest max
    a2 = make(sorted(range(0, N), key=lambda i: -arr[i]))  # next greatest min

    odd = [False] * N
    even = [False] * N
    odd[-1] = True
    even[-1] = True

    for i in range(N - 2, -1, -1):
      if a1[i] is not None:
        odd[i] = even[a1[i]]

      if a2[i] is not None:
        even[i] = odd[a2[i]]

    return sum(odd)
