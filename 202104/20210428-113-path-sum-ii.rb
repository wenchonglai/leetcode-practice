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
# @param {Integer} target_sum
# @return {Integer[][]}
def path_sum(root, target_sum)
  paths = []
  
  recurse(root, target_sum, paths, []) if root
  
  paths
end

def recurse(node, target_sum, paths, path)
  path << node.val
  paths << path.clone if node.val === target_sum && !node.left && !node.right
  recurse(node.left, target_sum - node.val, paths, path) if node.left
  recurse(node.right, target_sum - node.val, paths, path) if node.right
  path.pop
end