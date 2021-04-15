class RandomizedSet

    def initialize()
      @h = {}
      @a = []
    end

    def insert(val)
      if @h[val]
        return false
      else
        @h[val] = @a.length
        @a << val
        return true
      end
    end

    def remove(val)
      if @h[val]
        @h[@a.last] = @h[val]
        @a[@h[val]] = @a.last
        @a.pop
        @h.delete(val)
        return true
      else
        return false
      end
    end

    def get_random()
      return @a[rand(0...@a.length)]
    end


end

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()