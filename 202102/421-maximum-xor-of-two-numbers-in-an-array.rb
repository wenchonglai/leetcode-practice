def find_maximum_xor(nums)
  31.downto(0)
    .inject(0) do |max, digit|
      # max - 前 n 位最大值；temp_max - 假设第前 n + 1 位末位为 1 的前 n + 1 位最大值
      temp_max = max | (1 << digit)
      set = Set.new
      # 储存数组中各个数前 n + 1 位数值（见脚注）
      nums.each {|num| set << (num & temp_max)}
      # 若存在两数值，其前 n + 1 位的 XOR 等于 temp_max，则更新 max (设其第 n + 1 位为 1)
      max = set.any?{ |elem| set.include?(elem ^ temp_max) } ? temp_max : max
      # 否则，将 max 作为前 n + 1 位最大值 (其第 n + 1 位为 0)
    end
end

# 脚注：
# 理论上某数字前 n + 1 位数值的计算方法应为 set & 1111..10000000
# 但当我们知道所有数字两两 XOR 的前 n + 1 位最大值不超过 temp_max = 110101.... 的前提下，
# 可以反证: 若存在 i < n, temp_max 第 i 位为 0
# 则任一数字的第 i 位是 1 或 0 均不影响结果（因为已确定最大 XOR 值的第 i 位是 0）