def bsearch(arr, target, &prc)
  l = 0
  r = arr.length
  
  while l < r
    m = (l + r) / 2
    if prc.call(arr[m], target) < 0
      l = m + 1
    else
      r = m
    end
  end
  
  l
end

def insert(intervals, new_interval)
  l = bsearch(intervals, new_interval){|a, b| a[1] <=> b[0]}
  r = bsearch(intervals, new_interval){|a, b| (a[0] - 0.5) <=> b[1]} - 1

  new_interval[0] = intervals[l][0] if l < intervals.length && intervals[l][0] < new_interval[0]
  new_interval[1] = intervals[r][1] if r >= 0 && intervals[r][1] > new_interval[1]

  intervals[0...l] + [new_interval] + (intervals[r+1..-1] || [])
end