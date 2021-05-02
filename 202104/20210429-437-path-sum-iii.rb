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
# @return {Integer}
def path_sum(root, target_sum)
  @ct = 0
  traverse(root, 0, target_sum, Hash.new(0))
  @ct
end

def traverse(node, sum, target_sum, h)
  return 0 if !node
  
  sum += node.val
  @ct += 1 if sum === target_sum
  @ct += h[sum - target_sum]
  h[sum] += 1

  traverse(node.left, sum, target_sum, h)
  traverse(node.right, sum, target_sum, h)
  
  h[sum] -= 1
end