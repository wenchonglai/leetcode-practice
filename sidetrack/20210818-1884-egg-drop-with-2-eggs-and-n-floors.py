class Solution:
  def twoEggDrop(self, n: int) -> int:
    a = int((2 * n) ** 0.5)

    return a if n <= a * (a + 1) / 2 else a + 1
