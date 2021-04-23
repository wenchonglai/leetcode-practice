# @param {Integer[]} nums
# @return {Integer[]}

class Node
  attr_accessor :val, :left, :right
  
  def initialize(val, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class SegmentTree
  def initialize(arr)
    @len = arr.length
    @arr = arr
    @root = build
  end
  
  def query(s, e, l = 0, r = @len - 1, node = @root)
    if !node || e < s
      return 0
    elsif l >= r || s <= l && e >= r
      return node.val
    else
      m = (l + r) / 2
      if e <= m
        return query(s, e, l, m, node.left)
      elsif s > m
        return query(s, e, e, m + 1, node.left)
      else
        return query(s, m, l, m, node.left) + query(m + 1, e, m + 1, r, node.right)
      end
    end
  end
  
  def increment(i, l = 0, r = @len - 1, node = @root)    
    if l == r
      node.val += 1 
      return node.val
    end
    
    m = (l + r) / 2
    
    if i <= m
      increment(i, l, m, node.left)
    else
      increment(i, m + 1, r, node.right)
    end

    node.val = node.left.val + node.right.val
  end
  
  def get_val(node = @root)
    if (node.left || node.right)
      return get_val(node.left) + get_val(node.right)
    else
      return [node.val]
    end
    
  end
  
  private
  def build(l = 0, r = @len - 1)
    if (l >= r)
      node = Node.new(@arr[l])
    else
      m = ( l + r ) / 2

      left = build(l, m)
      right = build(m + 1, r)
      node = Node.new(left.val + right.val, left, right)
    end
  end
end

def count_smaller(nums)
  rank = {}
  ct = 0
  
  nums.sort.map.with_index do |num, i|
    if !rank[num]
      rank[num] = ct
      ct += 1
    end
  end
  
  tree = SegmentTree.new([0] * rank.size)
  res = []

  nums.reverse.each do |num|
    # 1, 1, 0, 1
    tree.increment(rank[num])
    res << tree.query(0, rank[num] - 1)
  end
  
  res.reverse
end