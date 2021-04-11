# @param {Integer[]} nums
# @return {Integer}

def comb(total, n)
  (total - n + 1..total).inject{|acc, el| acc * el} / (1..n).inject{|acc, el| acc * el}
end

class Node
  attr_accessor :val, :left, :right
  
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
  
  def calc
    if !@left && !@right
      return [1, 1]
    elsif !@right
      c, n = @left.calc
      return [c, n + 1]
    elsif !@left
      c, n = @right.calc
      return [c, n + 1]
    else
      c1, n1 = @left.calc
      c2, n2 = @right.calc
      return [c1 * c2 * comb(n1 + n2, n1), n1 + n2 + 1]
    end
  end
  
  def add(val)
    if val < @val
      if @left
        @left.add(val)
      else
        self.left = Node.new(val)
      end
    else
      if @right
        @right.add(val)
      else
        self.right = Node.new(val)
      end
    end
  end
end

def num_of_ways(nums)
  tree = Node.new(nums[0])
  
  nums[1..-1].each do |num|
    tree.add(num)
  end

  (tree.calc[0] - 1) % (10 ** 9 + 7)
end