def lowest_common_ancestor(root, p, q)
  #情况 A - 如果 p 和 q 均不在以 root 为根的树中，则返回 nil
  #情况 B - 如果 p 或 q 之一在以 root 为根的树中，则返回 p 或 q 至 root 的距离的负值
  #情况 C - 如果 p 和 q 都在以 root 为根的树中，则返回 p 至 root 的距离以及 q 至 root 的距离之和

  return nil if root.nil? # 情况 A0 - root 不存在
  return 0 if p == q      # 情况 C0 - p 和 q 为同一节点

  l = lowest_common_ancestor(root.left, p, q)
  r = lowest_common_ancestor(root.right, p, q)
  
  return ( l ? -l : ( r ? -r : -1 ) ) + 1 if root == p || root == q #情况 C1；p 和 q 其一为 root 节点，另一在 root 的子树中
  return nil if !l && !r                                            #情况 A1
  return l || r if l && l > 0 || r && r > 0                         #情况 C2；p 和 q 均在 root 的左子树或右子树中
  return -l - r + 2 if l && r                                       #情况 C3；p 和 q 其一在 root 的左子树中，另一在 root 的右子树中
  return ( l ? l : r ) - 1                                          #情况 B；节点距离 +1 （节点距离的负值 -1）
end

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

_tree = [3,5,1,6,2,0,8,nil,nil,7,4].map{|val| val ? TreeNode.new(val) : nil}; #(1..5000).zip(Array.new(5000, nil)).flatten

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
p lowest_common_ancestor(root, TreeNode.new(6), TreeNode.new(8))