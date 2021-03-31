def min_eating_speed(piles, h)
  l = 1
  r = piles.max
  
  while l < r
    m = (l + r) / 2
    
    if piles.map{|pile| (pile + m - 1) / m}.sum > h
      l = m + 1
    else
      r = m
    end
  end
  
  l
end