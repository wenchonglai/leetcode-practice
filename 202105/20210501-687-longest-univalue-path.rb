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
def longest_univalue_path(root)
  @ct = 0
  
  traverse(root)
  
  @ct
end

def traverse(root)
  return 0 if !root
  
  l = traverse(root.left)
  r = traverse(root.right)
  
  left = (!root.left || root.left.val != root.val) ? 0 : l
  right = (!root.right || root.right.val != root.val) ? 0 : r

  max = left + right

  @ct = [max, @ct].max
  
  return 1 + [left, right].max
end