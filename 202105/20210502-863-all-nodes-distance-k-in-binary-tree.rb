# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} target
# @param {Integer} k
# @return {Integer[]}
def distance_k(root, target, k)
  @vals = []
  
  dfs(root, target, [], k)
end

def dfs(node, target, path, k)
  return unless node
    
  path << node
  
  if node === target
    set = Set.new([nil])
    diff = 0
    
    until path.empty? || k < 0
      n = path.pop
      @vals += bfs(n, k, set)
      k -= 1
    end
  else
    dfs(node.left, target, path, k)
    dfs(node.right, target, path, k)
  end
  
  path.pop
  
  @vals
end

def bfs(node, k, set)
  q = [node]
  set << node

  until q.empty? || k == 0
    q = q.reduce([]) do |acc, el|
      acc << el.left unless set.include?(el.left)
      acc << el.right unless set.include?(el.right)
      acc
    end
    
    k -= 1
  end
  
  q.map(&:val)
end