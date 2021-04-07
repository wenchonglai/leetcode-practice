
def flip_match_voyage(root, voyage)
  treeStack = [root]
  arr = voyage.reverse
  res = []
  
  until treeStack.empty? || arr.empty?
    val = arr.pop
    node = treeStack.pop
    
    return [-1] if node.val != val
    
    if node.left && node.right
      if node.left.val == arr.last
        treeStack.push(node.right, node.left)
      else
        res << val
        treeStack.push(node.left, node.right)
      end
    else
      treeStack << node.right if node.right
      treeStack << node.left if node.left
    end
  end
  
  return [-1] unless treeStack.empty? && arr.empty?
  return res;
end