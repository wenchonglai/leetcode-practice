class LFUCache
  def initialize(capacity)
    @capacity = capacity
    @length = 0
    @h_val = {}
    @h_freq = Hash.new(0)
    @h_rev = Hash.new{|h, k| h[k] = Set.new}
    @min = nil
  end

  def get(key)
    if @h_val.has_key?(key)
      increase_freq(key)
      return @h_val[key]
    else
      return -1
    end
  end

  def put(key, value)
    return if @capacity <= 0
    
    if @h_val.has_key?(key)
      @h_val[key] = value
      increase_freq(key)
    else
      if @length === @capacity
        min_key = @h_rev[@min].first
        @h_val.delete(min_key)
        @h_freq.delete(min_key)
        @h_rev[@min].delete(min_key)
        @h_rev.delete(@min) if @h_rev[@min].empty?
      else
        @length += 1
      end
      
      @h_val[key] = value
      @h_freq[key] = 1
      @h_rev[1] << key
      @min = 1
    end
    
    nil
  end
  
  private
  def increase_freq(key)
    freq = @h_freq[key]
    min_in_freq = freq == @min
    
    @h_freq[key] += 1
    @h_rev[freq].delete(key)
    @h_rev.delete(freq) if @h_rev[freq].empty?
    @h_rev[freq + 1] << key

    @min += 1 if min_in_freq && !@h_rev.has_key?(freq)
  end
end