def recover_from_preorder(s)
  arr = s.split(/(\-+)/).inject([[0]]) do |acc, el|
    if acc.last.length == 2
      acc << [el.length]
    else
      acc.last.unshift(el.to_i)
    end
    
    acc
  end
  
  tree = TreeNode.new(arr[0][0]);
  nodes = [tree]
  ct = [2]
  
  arr[1..-1].each do |(val, depth)|
    node = TreeNode.new(val)
    
    until depth == ct.length
      ct.pop
      nodes.pop
    end
    
    lastCt = ct.last
    if lastCt == 2
      nodes.last.left = node
    elsif lastCt == 1
      nodes.last.right = node
    end

    
    ct[-1] -= 1
    ct << 2
    nodes << node
  end

  tree
end