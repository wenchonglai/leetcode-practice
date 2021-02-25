class WordDictionary

    def initialize(char = '')
      @char = char
      @children = {}
    end

    def add_word(word, is_new_word = true)
      if word.empty?
        @children[""] = false
        return
      end
      
      ch, substr = word[0], word[1..-1]
      
      @children[ch] = WordDictionary.new(ch) unless @children[ch]
      
      @children[ch].add_word(word[1..-1], false)
    end

    def search(word)
      ch, substr = word[0], word[1..-1]

      if (word.empty?)
        return @children[""] == false
      elsif (ch == '.')
        return @children ? @children.any?{|_, child| child && child.search(substr) } : false
      else
        node = @children[ch]
        return true if node && node.search(substr)
      end
      
      false
    end
  
end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary.new()
# obj.add_word(word)
# param_2 = obj.search(word)