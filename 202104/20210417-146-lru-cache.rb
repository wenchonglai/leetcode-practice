class Node
  attr_reader :val, :prev, :next;
  
  def initialize(val = nil)
    @val = val
    @prev = nil
    @next = nil
  end
  
  def detach
    self.prev.next = self.next if self.prev
    self.next.prev = self.prev if self.next
    self.prev = nil
    self.next = nil
    self
  end
  
  def append(node)
    node.detach
    
    self.next.prev = node if self.next
    node.next = self.next
    self.next = node
    node.prev = self
  end
  
  protected
  attr_writer :next, :prev
end

class DQueue
  
  def initialize
    @head = Node.new
    @tail = Node.new
    
    @head.append(@tail)
  end
  
  def <<(node)
    @tail.prev.append(node)
  end
  
  def shift
    unless empty?
      @head.next.detach
    end
  end
  
  def empty?
    @head.next == @tail
  end
end

class LRUCache

  def initialize(capacity)
    @size = 0
    @capacity = capacity
    @h = {}
    @q = DQueue.new
  end

  def get(key)
    node = @h[key]
    
    if node
      node.detach
      @q << node
      node.val[1]
    else
      -1
    end
    
  end

  def put(key, value)
    node = @h[key]
    
    if node
      node.detach
      node.val[1] = value
    else
      node = Node.new([key, value])
      @h[key] = node
      @size += 1
      trim
    end
    
    @q << node
  end
  
  private
  def trim
    until @size <= @capacity
      key, _ = @q.shift.val
      
      @h[key] = nil
      @size -= 1
    end
  end
end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)