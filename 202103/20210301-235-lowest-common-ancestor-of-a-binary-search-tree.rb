def lowest_common_ancestor(curr, p, q)
  while curr
    return curr if ( p.val - curr.val ) * ( q.val - curr.val ) <= 0
    curr = p.val > curr.val ? curr.right : curr.left
  end
  
  curr.val
end