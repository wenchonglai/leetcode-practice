class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
    def ==(node)
      @val == node.val
    end
end

def in_tree(root, p)
  root && root == p || root && ( in_tree(root.left, p) || in_tree(root.right, p) )
end

def _lca_exist(root, p, q)
  return root if root.nil? || root == p || root == q
  
  l = _lca_exist(root.left, p, q)
  r = _lca_exist(root.right, p, q)
  
  l && r && root || l || r
end

def lowest_common_ancestor(root, p, q)
  return nil unless in_tree(root, p) && in_tree(root, q)

  _lca_exist(root, p, q)
end


_tree = (1..5000).zip(Array.new(5000, nil)).flatten.map{|val| val ? TreeNode.new(val) : nil}

root = _tree.shift
arr = [root]

until arr.empty?
  arr.each do |curr|
    curr = arr.shift
    curr.left = _tree.shift
    curr.right = _tree.shift
    arr << curr.left if curr.left
    arr << curr.right if curr.right
  end
end

p 'start'
p lowest_common_ancestor(root, TreeNode.new(4999), TreeNode.new(5001)).val
