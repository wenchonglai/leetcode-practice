class Solution:
  def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
    h = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    h1 = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a', 'c': True}
    ct = 0
    mx = 0

    for ch in croakOfFrogs:
      if ch not in h1:
        return -1

      h[ch] += 1

      if ch == 'c':
        ct += 1
        mx = max(ct, mx)
      else:
        if h[h1[ch]] == 0:
          return -1

        h[h1[ch]] -= 1
        if ch == 'k':
          h[ch] -= 1
          ct -= 1

    return mx if not [k for k in h if h[k]] else -1