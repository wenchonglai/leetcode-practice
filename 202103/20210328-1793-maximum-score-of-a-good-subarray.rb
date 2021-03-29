def maximum_score(nums, k)
  min = nums[k]
  max = nums[k]
  len = nums.length
  i = k
  j = k
  
  while (i >= 0 && j < len)
    min = [ nums[i], nums[j], min ].min
    max = [ min * (j - i + 1), max ].max
    
    l = nums[i - 1] || min
    r = nums[j + 1] || min

    if (!nums[j + 1] || i > 0 && l > r)
      i -= 1
    else
      j += 1
    end
  end
  
  max
end