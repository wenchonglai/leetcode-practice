def merge(intervals)
  arr = []
  
  intervals.sort{|a, b| a[0] <=> b[0]}.each do |interval|
    if arr.empty? || interval[0] > arr[-1][1]
      arr << interval 
    else
      arr[-1][1] = interval[1] if interval[1] > arr[-1][1]
    end
  end
    
  arr
end