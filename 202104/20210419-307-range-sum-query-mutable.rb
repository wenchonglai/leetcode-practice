class NumArray
  def initialize(nums)
    len = nums.length
    @data = [nums]
    
    while len > 1
      len = (len + 1) / 2
      @data << (0...len).map{|i| @data[-1][i * 2] + (@data[-1][i * 2 + 1] || 0)}
    end
  end

  def update(index, val)
    val0 = @data[0][index]
    diff = val - val0
    
    (0...@data.length).each do |i|
      @data[i][index] += diff
      index /= 2
    end
  end

  def sum_range(left, right)
    sum(right) - sum(left - 1)
  end

  private def sum(index)
    sum = 0
    i = 0
    
    while index >= 0
      sum += @data[i][index] if index % 2 === 0
      i += 1
      index = (index - 1) / 2
    end
    
    sum
  end
end