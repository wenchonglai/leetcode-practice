class Solution(object):
  def findRLEArray(self, encoded1, encoded2):
    """
    :type encoded1: List[List[int]]
    :type encoded2: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    N1 = len(encoded1)
    N2 = len(encoded2)
    i1, i2 = 0, 0
    ct1, ct2 = 0, 0

    while i1 < N1 and i2 < N2:
      if ct1 == 0:
        [val1, ct1] = encoded1[i1]

      if ct2 == 0:
        [val2, ct2] = encoded2[i2]
    
      prod = val1 * val2
      delta = min(ct1, ct2)
      ct1 -= delta
      ct2 -= delta

      if ct1 == 0:
        i1 += 1
      
      if ct2 == 0:
        i2 += 1
      
      if res and res[-1][0] == prod:
        res[-1][1] += delta
      else:
        res.append([prod, delta])
    
    return res

s = Solution()

print(s.findRLEArray([[1, 3], [2, 1], [3, 2]], [[2, 3], [3, 3]]))
