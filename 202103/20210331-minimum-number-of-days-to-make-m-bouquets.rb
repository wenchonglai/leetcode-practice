# @param {Integer[]} bloom_day
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_days(bloom_day, m, k)
  return -1 if m * k > bloom_day.length
  
  l = bloom_day.min
  r = bloom_day.max
  
  while l < r
    mid = (l + r) / 2
    
    flower = 0
    bouquet = 0
    
    bloom_day.each do |day|
      if day <= mid
        flower += 1 
      else
        flower = 0
      end
      
      if (flower == k)
        flower = 0
        bouquet += 1
      end

    end

    if bouquet < m
      l = mid + 1
    else
      r = mid
    end
    
  end
  
  return l
end