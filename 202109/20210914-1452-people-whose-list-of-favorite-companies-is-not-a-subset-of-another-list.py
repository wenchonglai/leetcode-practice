class Solution:
  def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
    pool = set()
    n = len(favoriteCompanies)

    for sub in favoriteCompanies:
      for el in sub:
        pool.add(el)

    h = {el: i for (i, el) in enumerate(pool)}

    def gen(sub):
      val = 0
      nonlocal h

      for el in sub:
        val |= 1 << h[el]

      return val

    arr = [gen(sub) for sub in favoriteCompanies]
    res = [True] * n

    for i in range(0, n):
      vi = arr[i]
      for j in range(0, i):
        vj = arr[j]
        val = vi | vj

        if val == vi:
          res[j] = False
        elif val == vj:
          res[i] = False

    return [i for i in range(n) if res[i]]
