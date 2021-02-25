class WordFilter

  def initialize(words)
    @hash_pre = Hash.new{|h, k| h[k] = []}
    @hash_next = Hash.new{|h, k| h[k] = []}
    
    words.each_with_index do |word, i|
      len = word.length
      
      @hash_pre[word] << i
      @hash_next[word] << i
      
      (1...word.length).each do |j|
        @hash_pre[word[0...j]] << i
        @hash_next[word[j..-1]] << i
      end
    end
  end

  def f(prefix, suffix)
    pre = @hash_pre[prefix].dup
    suf = @hash_next[suffix].dup

    until pre.empty? || suf.empty?
      last_p = pre.last
      last_s = suf.last
      
      return last_p if last_p == last_s
      
      (last_p > last_s ? pre : suf).pop
    end
    
    return -1
  
  end
end