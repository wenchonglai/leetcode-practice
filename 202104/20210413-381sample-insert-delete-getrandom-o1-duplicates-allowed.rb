class RandomizedCollection

=begin
    Initialize your data structure here.
=end
    def initialize()
      @h = Hash.new{|h, v| h[v] = Set.new}
      @a = []
    end


=begin
    Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def insert(val)
      notContained = @h[val].empty?
      
      @h[val] << @a.length
      @a << val

      notContained
    end


=begin
    Removes a value from the collection. Returns true if the collection contained the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def remove(val)
      # 把最后一个元素移到第一个 val 出现的位置，并且删除 val
      # 如果最后一个元素恰好也是 val，那么不需要把最后一个元素加回去
      return false if @h[val].empty?
      
      val_first_index = @h[val].first
      last_item = @a[-1]
      is_last_index = val_first_index == @a.length - 1
      
      @h[val].delete(val_first_index)
      @h[last_item].delete(@a.length - 1)
      @h[last_item] << val_first_index unless is_last_index
      @a.pop
      @a[val_first_index] = last_item unless is_last_index

      true
    end


=begin
    Get a random element from the collection.
    :rtype: Integer
=end
    def get_random()
      return @a.sample
    end


end

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()