class AllOne
  def initialize()
    @h_freq = Hash.new{|h, k| h[k] = 0}
    @h_rank = Hash.new{|h, k| h[k] = Set.new}
    @min = 0
    @max = 0
    @length = 0
  end

  def inc(key)
    @length += 1
    
    if @h_freq[key].zero?
      @h_freq[key] = 1
      @h_rank[1] << key
      @min = 1
      @max = 1 if @max == 0
    else
      freq = @h_freq[key]
      @h_freq[key] += 1
      @h_rank[freq].delete(key)
      @h_rank.delete(freq) if @h_rank[freq].empty?
      @h_rank[freq + 1] << key
      @max = [freq + 1, @max].max
      
      @min += 1 unless @h_rank.has_key?(@min)
    end
    
    nil
  end

  def dec(key)
    if @h_freq[key].zero?
      return
    else
      @length -= 1
      
      freq = @h_freq[key]
      @h_freq[key] -= 1
      @h_rank[freq].delete(key)
      @h_rank.delete(freq) if @h_rank[freq].empty?
      @h_rank[freq - 1] << key if freq > 1
      
      if !@h_rank.has_key?(@min)
        if @length > 0
          @min = @h_rank.keys.min
        else
          @min = 0
        end
      end
        
      @max = @h_rank[@max].empty? ? @max - 1 : @max
    end
    
    nil
  end

  def get_min_key()
    @h_rank[@min].empty? ? '' : @h_rank[@min].first
  end

  def get_max_key()
    @h_rank[@max].empty? ? '' : @h_rank[@max].first
  end
end

# Your AllOne object will be instantiated and called as such:
# obj = AllOne.new()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.get_max_key()
# param_4 = obj.get_min_key()