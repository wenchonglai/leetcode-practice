class NumArray:

    def __init__(self, nums: List[int]):
      self.arr = [0]
      acc = 0

      for num in nums:
        acc += num
        self.arr.append(acc)

    def sumRange(self, left: int, right: int) -> int:
      return self.arr[right + 1] - self.arr[left]
