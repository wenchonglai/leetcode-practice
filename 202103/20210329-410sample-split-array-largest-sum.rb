# 整体思路：
# 二分搜索，左边为最大元素值（子序列和不可能小于最大元素），右边为所有元素和
# 左右取中值；遍历元素，获取最大子序列和不大于中值时的最小子序列个数
# 如果最小子序列个数大于给定的 m（即当子序列数量为 m 时，最小子序列和大于当前中值），则左边界右移
# 否则右边界左移

def split_array(nums, m)
  l = nums.max #这里必须是 nums.max，不能是 0，否则即使子序列长度为 1，最小子序列和也小于 l
  r = nums.sum
  
  while l < r
    mid = (l + r) / 2
    sum = 0
    count = 1
    
    nums.each do |num|
      if sum + num > mid
        count += 1
        sum = num
      else
        sum += num
      end
    end
    
    if count > m
      l = mid + 1
    else
      r = mid
    end

  end
  
  return l
end