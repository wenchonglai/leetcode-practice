class Solution:
  def longestAwesome(self, s: str) -> int:
    # 思路：prefix sum + bitmask
    # 0-9只有10个数字，每个数字转化为二进制的相应位数
    # 从第一个字符遍历到最后
    #   对出现的所有字符进行编码：出现单数次则位数为1，双数次则位数为0
    #   若同一编码重复出现在索引i1，i2，
    #     则i1至i2间各字符都只出现偶数次
    #   对编码和2^0至2^9取异或；若取完异或的编码出现在i3(i3<i2)；
    #     则i3-i2间只存在一个字符出现过奇数次

    N = len(s)
    code = 0
    m = 0
    h = {0: 0}

    for i in range(0, N):
      code ^= 1 << int(s[i])

      if code not in h:
        h[code] = i + 1

      if i + 1 - h[code] > m:
        m = i + 1 - h[code]

      for j in range(0, 10):
        alt_code = code ^ (1 << j)

        if alt_code in h and i + 1 - h[alt_code] > m:
          m = i + 1 - h[alt_code]

    return m