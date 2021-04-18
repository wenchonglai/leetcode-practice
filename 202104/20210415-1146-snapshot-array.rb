class SnapshotArray
  def initialize(length)
    @h = Hash.new{|h, k| h[k] = {};}
    
    (0...length).each {|i| @h[i][0] = 0 }
    
    @ct = 0
  end

  def set(index, val)
    @h[index][@ct] = val
  end

  def snap()
    @ct += 1
    @ct - 1
  end

  def get(index, snap_id)
    keys = @h[index].keys
    l = 0
    r = keys.length - 1
    
    while l < r
      m = (l + r) / 2

      if keys[m] == snap_id
        return @h[index][keys[m]]
      elsif keys[m + 1] <= snap_id
        l = m + 1
      else
        r = m
      end
    end

    return @h[index][keys[l]]
  end
end

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray.new(length)
# obj.set(index, val)
# param_2 = obj.snap()
# param_3 = obj.get(index, snap_id)