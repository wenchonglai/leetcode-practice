# @param {Integer[]} arr
# @return {Integer}
# @param {Integer[]} nums
# @return {Integer}

# @param {Integer[]} arr
# @return {Integer}

def find_length_of_shortest_subarray(nums)
  len = nums.length 
  l = 0
  r = len
  
  # 左指针移动到第一个极大值
  l += 1 until l + 1 >= len || nums[l + 1] < nums[l]
  
  # 需要删除的区间长度初始化为第一个极大值右边的元素个数
  res = r - l - 1
  
  # 右指针向左移动，直至出现极小值
  # r == len - 1 时 nums[r] == nil，无法比较大小，因此引入 INFINITY
  until r <= 0 || nums[r - 1] > (nums[r] || Float::INFINITY) 
    r -= 1

    #右指针每左移一位，不断将左指针左移，使其指向元素不大于右指针指向元素
    l -= 1 until l < 0 || nums[l] <= nums[r] 

    # 计算左右指针之间元素数量，若小于 res 则更新 res
    res = [r - l - 1, res].min 
  end
  
  # res 有可能为负，为负时返回0
  [res, 0].max
end