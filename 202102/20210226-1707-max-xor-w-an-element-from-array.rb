# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
class Trie
  def initialize(digits)
    @root = []
    @digits = digits
  end
  
  def insert(num)
    node = @root
    
    @digits.downto(0).each do |digit|
      node[2] = num unless node[2] && node[2] < num
      mask = 1 << digit
      index = (num & mask).zero? ? 0 : 1
      
      node[index] ||= []
      node = node[index]
    end
    
    node[2] = num
  end
  
  def search_xor(num1, num2)
    node = @root
    
    @digits
      .downto(0)
      .each do |digit|
        return -1 unless node

        mask = 1 << digit
        
        if !node[1] || node[1][2] > num2
          node = node[0]
          next
        end

        index = (num1 & mask).zero? ? 1 : 0

        node = node[index] || node[index ^ 1]
      end
    
    node ? num1 ^ node[2] : -1
  end
end


def maximize_xor(nums, queries)
  t = Trie.new( Math.log2(nums.max).to_i )
  
  nums.each {|num| t.insert(num)}
  
  queries.map do |pair|
    t.search_xor(*pair)
  end
end