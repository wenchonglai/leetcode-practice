# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def num_subseq(nums, target)
  mod = 10 ** 9 + 7
  arr = nums.select{|n| n <= target}.sort
  l = arr.length
  exps = Array.new(l, 1)
  count = 0
  
  for i in (1...l)
    exps[i] = exps[i - 1] * 2 % mod #先储存2的幂，避免每次重复计算
  end

  j = l - 1

  for i in (0...l)
    j -= 1 until j < i or arr[i] + arr[j] <= target

    return count if j < i
      
    count += exps[j - i] 
    count %= mod
  end
    
  count
end