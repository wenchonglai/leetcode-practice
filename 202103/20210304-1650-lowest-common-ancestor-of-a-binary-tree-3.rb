def lowestCommonAncestor(p, q)
  h = {}

  while p
    h[p] = true
    p = p.parent
  end

  while q
    return q if h[q]
    q = q.parent
  end
end
