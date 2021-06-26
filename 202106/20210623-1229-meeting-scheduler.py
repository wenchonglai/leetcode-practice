
class Solution(object):
  def minAvailableDuration(self, slots1, slots2, duration):
    i1, i2, l1, l2 = 0, 0, len(slots1), len(slots2)

    while i1 < l1 and i2 < l2:
      [s1, e1] = slots1[i1]
      [s2, e2] = slots2[i2]

      if e1 < s2:
        i1 += 1
        continue

      if e2 < s1:
        i2 += 1
        continue
        
      _min = max(s1, s2)
      _max = min(e1, e2)

      i1 += 1
      i2 += 1

      if _max - _min >= duration:
        return [_min, _min + duration]

    return []
