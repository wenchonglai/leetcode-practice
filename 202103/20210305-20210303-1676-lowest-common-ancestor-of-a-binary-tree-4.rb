def lowest_common_ancestor(root, nodes)
  return nil unless root
  return root if nodes.any?{|node| root.val == node.val }
  
  l = lowest_common_ancestor(root.left, nodes)
  r = lowest_common_ancestor(root.right, nodes)
  
  l && r && root || l || r
end

