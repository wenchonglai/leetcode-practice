# @param {Integer[][]} points
# @return {Integer}
def find_min_arrow_shots(points)
  count = 0
  curr = nil
  
  points
    .sort{|a, b| a[1] <=> b[1]}
    .each do |point|
      unless curr && point[0] <= curr[1]
        curr = point
        count += 1
      end
    end
  
  count
end