# notes
# 1 - using loop is faster than using recursion
# 2 - instantiating a simple hash as a child node is faster than instantiating a Trie instance

class Trie
  def initialize()
    @node = {children: {}}
  end

  def insert(word)
    node = @node
    
    word.each_char do |ch|
      node[:children][ch] ||= {children: {}}
      node = node[:children][ch]
    end
    
    node[:is_end] = true
  end

  def search(word)
    node = @node
    
    word.each_char do |ch|
      return false unless node[:children][ch]
      node = node[:children][ch]
    end
    
    !!node[:is_end]
  end

  def starts_with(prefix)
    node = @node
    
    prefix.each_char do |ch|
      return false unless node[:children][ch]
      node = node[:children][ch]
    end
    
    true
  end
  
  
end

# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)