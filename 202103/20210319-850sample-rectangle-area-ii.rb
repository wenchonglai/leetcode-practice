# @param {Integer[][]} rectangles
# @return {Integer}

# 思路：矩形水平边按照 y 值大小排序
# 每插入/删除一条水平边后，重新计算之前水平边总长度 x (当前 y 值 - 之前 y 值)
#   用有序数组存储当前各水平边；查找复杂度为 O(logN)，插入/删除复杂度为 O(N)
# 各个面积加起来为图形总面积
# 一共加入/删除 2n 条水平边，时间复杂度 O(N^2)

def rectangle_area(rectangles)
  intervals = []
  baseline = []
  
  rectangles.each do |(x0, y0, x1, y1)|
    intervals << [y0, x0, x1, true]
    intervals << [y1, x0, x1, false]
  end
  
  intervals.sort!{|a, b| a[0] <=> b[0]}
  
  y_prev = intervals[0][0]
  len_prev = 0
  area = 0

  intervals.each do |(y, x0, x1, start)|
    i = bsearch(baseline, [x0, x1])
    
    if (start)
      baseline.insert(i, [x0, x1])
    else
      baseline.delete_at(i)
    end

    len = recalc(baseline)
    area += len_prev * (y - y_prev)
    area %= ( 10 ** 9 + 7 )
    y_prev = y;
    len_prev = len
  end
  
  area
end

def recalc(baseline)
  return 0 if baseline.empty?
  
  curr = baseline[0]
  len = 0
  
  baseline[1..-1].each do |interval|
    if interval[0] >= curr[1]
      len += curr[1] - curr[0]
      curr = interval
    else
      curr = [curr[0], [curr[1], interval[1]].max]
    end
  end
  
  len + curr[1] - curr[0]
end

def bsearch(arr, target)
  l = 0
  r = arr.length - 1
  
  while l <= r
    m = (l + r) / 2
    res1 = arr[m][0] <=> target[0]
    
    if res1 === 0
      res2 = arr[m][1] <=> target[1]
      
      if res2 === 0
        return m
      elsif res2 < 0
        l = m + 1
      else
        r = m - 1
      end
    elsif res1 < 0
      l = m + 1
    else
      r = m - 1
    end
  end
  
  l
end