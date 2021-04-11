def ship_within_days(weights, d)
  l = weights.max
  r = weights.sum
  
  while l < r
    m = (l + r) / 2
    
    days = 1
    acc = 0
    
    weights.each do |weight|
      if acc + weight > m
        acc = weight
        days += 1
      else
        acc += weight
      end
    end
      
    if days > d
      l = m + 1
    else
      r = m
    end
      
  end
  
  l
end
