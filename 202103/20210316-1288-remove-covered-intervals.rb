def remove_covered_intervals(intervals)
  # 思路：按 interval 区间左端点大小排序
  # 如果：
  # 1. 某区间右端点大于指针区间的右端点（否则当前区间被指针区间覆盖），且
  # 2. 左端点大于指针区间的左端点（否则，指针区间被当前区间覆盖，需要从数组中删除）
  # 则该区间和指针区间不相互覆盖，因此更新指针区间为当前区间，不被覆盖的 count + 1

  intervals = intervals.sort{|a, b| a[0] <=> b[0]};
  count = 1;
  curr = intervals[0];
  
  (1...intervals.length).each do |i|
    if (intervals[i][1] > curr[1])
      count += 1 if intervals[i][0] > curr[0]
      curr = intervals[i]
    end
  end
  
  count
end