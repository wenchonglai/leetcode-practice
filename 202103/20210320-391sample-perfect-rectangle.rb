def is_rectangle_cover(rectangles)
  # 思路：小矩形构成不重叠的大矩形当且仅当：
  # 1 - 包含所有小矩形的大矩形面积等于各小矩形面积之和
  # 2 - 包含所有小矩形的大矩形各顶点仅存在于至多一个小矩形中，且所有小矩形顶点中有且只有四个顶点出现一次
  # 3 - 没有位置相同面积相同的小矩形
  #     否则，下方矩形（各数字表示矩形在该位置出现的次数）满足条件 1 & 2：
  #       1 1 1
  #       1 0 1
  #       1 2 1

  x_min, y_min, x_max, y_max = Float::INFINITY, Float::INFINITY, -Float::INFINITY, -Float::INFINITY
  area = 0
  points = Hash.new(0)
  
  return false if rectangles.to_set.length != rectangles.length # 条件 3
  
  rectangles.each do |x0, y0, x1, y1|
    area += (x1 - x0) * (y1 - y0) # 累加各个小矩形面积
    x_min = [x_min, x0].min
    y_min = [y_min, y0].min
    x_max = [x_max, x1].max
    y_max = [y_max, y1].max
    
    points[[x0, y0]] += 1
    points[[x0, y1]] += 1
    points[[x1, y0]] += 1
    points[[x1, y1]] += 1
  end
  
  pts = points.select{|_, v| v == 1}
  
  pts.length == 4 &&
    [[x_min, y_min], [x_max, y_max], [x_min, y_max], [x_max, y_min]].all?{|pt| points[pt] == 1} && #条件 2
    area == (y_max - y_min) * (x_max - x_min) # 条件 1
end