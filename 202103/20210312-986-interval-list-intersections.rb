def interval_intersection(first_list, second_list)
  arr = []
  
  until first_list.empty? || second_list.empty?
    s = [first_list[0][0], second_list[0][0]].max
    e = [first_list[0][1], second_list[0][1]].min

    (e == first_list[0][1] ? first_list : second_list).shift 
    
    arr << [s, e] if s <= e
  end
  
  arr
end
