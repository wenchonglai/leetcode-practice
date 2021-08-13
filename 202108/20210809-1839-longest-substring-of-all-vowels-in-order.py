class Solution:
  def longestBeautifulSubstring(self, word: str) -> int:
    h = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    currIdx = 0
    i0 = None
    res = 0

    for (i, ch) in enumerate(word):
      if h[ch] < currIdx or h[ch] > currIdx + 1:
        if currIdx == 4 and i0 != None and res < i - i0:
          res = i - i0

        i0 = None

      if i0 == None and ch == "a":
        i0 = i

      currIdx = h[ch]

    if word[-1] == "u" and i0 != None and res < i + 1 - i0:
      res = i + 1 - i0

    return res
