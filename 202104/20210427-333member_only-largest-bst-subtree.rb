class Node
  attr_accessor :val, :left, :right
  def initialize(val, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def helper(node)
  val = node.val
  l_min, l_max, l_ct, l_max_ct = node.left ? helper(node.left) : [val, val, 0, 0]
  r_min, r_max, r_ct, r_max_ct = node.right ? helper(node.right) : [val, val, 0, 0]
    
  if l_ct.nil? || r_ct.nil? || l_max > val || r_min < val
    return [nil, nil, nil, [l_max_ct, r_max_ct].max]
  else 
    return [l_min, r_max, l_ct + r_ct + 1, l_ct + r_ct + 1]
  end
end

def largestBSTSubtree(root)
  helper(root)[3]
end

root = Node.new(10, 
  Node.new(5, 
    Node.new(1),
    Node.new(8)
  ),
  Node.new(15,
    Node.new(7)
  )
)

p largestBSTSubtree(root)