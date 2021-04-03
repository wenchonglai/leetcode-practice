# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def smallest_divisor(nums, threshold)
  l = 1
  r = nums.max
  
  while l < r
    m = (l + r) / 2
    ct = nums.inject(0) { |acc, num| acc + (num + m - 1) / m }
    
    if ct > threshold
      l = m + 1
    else
      r = m
    end
  end
  
  l
end