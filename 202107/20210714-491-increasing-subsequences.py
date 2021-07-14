class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    set_ = set()

    for num in nums:
      for sub in [*set_]:
        if sub[-1] > num:
          continue

        newSub = tuple([*sub, num])

        if newSub not in set_:
          set_.add(newSub)

      set_.add((num,))

    for num in nums:
      set_.discard((num,))

    return [list(i) for i in set_]
