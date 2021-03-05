def is_identical(a, b)
  return true unless a || b
  return false if a.nil? || b.nil? || a.val != b.val
  is_identical(a.left, b.left) && is_identical(a.right, b.right)
end

def is_subtree(s, t)
  is_identical(s, t) || s.left && is_subtree(s.left, t) || s.right && is_subtree(s.right, t) || false
end