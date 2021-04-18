class CustomStack

  def initialize(max_size)
    @max_size = max_size
    @data = []
    @inc = []
  end

  def push(x)
    @data << x if @data.length < @max_size
  end

  def pop()
    len = @data.length
    return -1 if len == 0
    
    if len > 1
      @inc[len - 1] ||= 0
      @inc[len - 2] ||= 0
      @inc[len - 2] += @inc[len - 1]
    end
    
    @data.pop + (@inc.pop || 0)
  end

  def increment(k, val)
    i = [k - 1, @data.length - 1].min
    @inc[i] = (@inc[i] || 0) + val if i >= 0
  end

end

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack.new(max_size)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k, val)