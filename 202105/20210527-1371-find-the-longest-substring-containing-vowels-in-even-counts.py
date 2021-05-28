class Solution:
  def findTheLongestSubstring(self, s: str) -> int:
    h = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    h1 = {}
    h1[0] = 0
    now = 0
    m = 0
    i = 0

    for ch in s:
      i += 1

      if ch in h:
        now ^= h[ch]

      if now not in h1:
        h1[now] = i
      elif i - h1[now] > m:
        m = i - h1[now]

    return m
