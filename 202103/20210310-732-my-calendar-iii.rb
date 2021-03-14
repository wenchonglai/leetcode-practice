def bsearch(arr, target, &prc)
  l = 0;
  r = arr.length;

  while (l < r) do 
    m = (l + r) / 2
    res = prc.call(arr[m], target)

    if res > 0
      r = m
    else
      l = m + 1
    end
  end

  l
end

class MyCalendarThree
    def initialize()
      @arr = []
      @counts = []
      @maxes = []
    end

    def book(start, e)
      l = bsearch(@arr, start){|a, b| a[0] <=> b}
      @arr.insert(l, [start, 1])
      @counts.insert(l, l.zero? ? 0 : @counts[l - 1])
      
      r = bsearch(@arr, e - 0.1){|a, b| a[0] <=> b}
      @arr.insert(r, [e, -1])
      @counts.insert(r, r.zero? ? 0 : @counts[r - 1])
      
      max = @maxes[-1] || 0

      (l...r).each do |i|

        @counts[i] += 1
        max = @counts[i] if @counts[i] > max
      end

      @maxes << max

      max
    end

end