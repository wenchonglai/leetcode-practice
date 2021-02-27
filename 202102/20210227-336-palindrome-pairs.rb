# @param {String[]} words
# @return {Integer[][]}
class Trie
  attr_reader :root
  
  def initialize
    @root = {}
  end
  
  def add(word, i)
    node = @root
    
    word.each_char do |ch|
      node[ch] ||= {}
      node = node[ch]
    end
    
    node[:index] = i
  end 
end

def all_palindrome_indices(root)
  queue = [['', root]]
  set = Set.new
  
  until queue.empty?
    substr, node = queue.shift
    
    if node[:index]
      set << node[:index] if substr == substr.reverse
    end
    
    node.each do |ch, child|
      next if ch == :index
      queue << [substr + ch, child]
    end
  end=
  
  set
end

def palindrome_pairs(words)
  prefix_trie = Trie.new
  suffix_trie = Trie.new
  
  words.each_with_index do |w, i|
    prefix_trie.add(w, i)
    suffix_trie.add(w.reverse, i)
  end
  
  queue = [[prefix_trie.root, suffix_trie.root]]
  set = Set.new

  until queue.empty?
    p_node, s_node = queue.shift
    p_i, s_i = p_node[:index], s_node[:index]
    
    if p_i
      all_palindrome_indices(s_node).each do |i|
        set << [p_i, i] if p_i != i
      end
    end
    
    if s_i
      all_palindrome_indices(p_node).each do |i|
        set << [i, s_i] if s_i != i
      end
    end
    
    p_node.each do |ch, child_node|
      next if ch == :index
      queue << [child_node, s_node[ch]] if s_node[ch]
    end
  end
  
  set.to_a
end