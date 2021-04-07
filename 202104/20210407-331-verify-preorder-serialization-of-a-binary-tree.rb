def is_valid_serialization(preorder)
  return true if preorder == '#';
  
  cts = []
  arr = preorder.split(',');
  i = 0
  len = arr.length
  
  while i < len
    if arr[i] == '#'
      return false if cts.empty?
      
      cts[-1] -= 1
      
      until cts.empty? || cts[-1] > 0
        cts.pop
        
        return i == len - 1 if cts.empty?
        cts[-1] -= 1
      end

    else
      cts << 2
    end

    i += 1
  end
  
  cts.empty?
end