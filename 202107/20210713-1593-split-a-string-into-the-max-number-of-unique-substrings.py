class Solution:
  def maxUniqueSplit(self, s: str) -> int:
    N = len(s)

    def helper(i, set_):
      max_ = 0

      for j in range(N, i, -1):
        sub = s[i:j]
        if sub not in set_:
          set_.add(sub)

          val = helper(j, set_)

          if max_ == 0 or max_ < val + 1:
            max_ = val + 1

          set_.discard(sub)

      return max_

    return helper(0, set())
