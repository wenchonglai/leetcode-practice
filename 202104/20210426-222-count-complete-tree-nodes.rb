# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}

def get_depth(node)
  depth = 0
  
  while node
    depth += 1
    node = node.left
  end
  
  depth
end

def count_nodes(root)
  return 0 if !root
  return 1 if !root.left
  return 2 if !root.right
  
  depth = get_depth(root)
  
  right_depth = 1 + get_depth(root.right)
  
  if right_depth === depth
    return 2 ** (depth - 1) + count_nodes(root.right) 
  else
    return 2 ** (depth - 2) + count_nodes(root.left)
  end
end