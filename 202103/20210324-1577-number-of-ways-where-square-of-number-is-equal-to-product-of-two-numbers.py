# collections 是 python 内置的容器类库，包含：
# - namedtuple - ('name', [attr1, attr2, ...])
# - deque 双向链表
# - defaultdict 带默认值的字典
# - OrderedDict key有序的字典
# - Counter 计数器
# - ...
from collections import defaultdict

class Solution:
  def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    def helper(h1, h2):
      count = 0
      
      # 遍历 h1 中元素
      for (n1, c1) in h1.items():
        sq = n1 * n1
        
        # 遍历 h2 中元素
        for (n2, c2) in h2.items():

          # 如果 sq 不能被 n2 整除，或者 n2 > n1 则跳过
          # （假设 n2 为成对元素中较小的那个，若 n2 > n1，则 n2 * n2_pair > n1 * n1）
          if sq % n2 == 0 and n2 <= n1:
            # 若 n2 = n1，且 h2 中存在 c2 个 n2，则 h2 中共存在 C(n2, 2) = (n2 * (n2 - 1)) / 2 个满足条件的对
            # 否则，若 h2[sq/n2] 存在且数量非 0，则 h2 中共存在 c2 * h2.get(sq / n2) 个满足条件的对
            count += c1 * ( c2 * (c2 - 1) // 2 if n1 == n2 else c2 * h2.get(sq / n2, 0) )
      
      return count
    
    # h1, h2 为字典，分别储存 nums1 和 nums2 中每个数字出现的次数
    h1 = defaultdict(int)
    h2 = defaultdict(int)
    
    for n in nums1:
      h1[n] += 1
      
    for n in nums2:
      h2[n] += 1
    
    # 用辅助函数分别计算 h2 中成对元素乘积与 h1 中元素平方相等的成对元素数量，以及
    # h1 中成对元素乘积与 h2 中元素平方相等的成对元素数量
    return helper(h1, h2) + helper(h2, h1)
