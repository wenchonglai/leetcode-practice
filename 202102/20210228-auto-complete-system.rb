class AutocompleteSystem
  def initialize(sentences, times)
    @h = Hash.new(0)
    @root = {}
    @curr = @root
    @sentence = ''

    sentences.zip(times).each { |pair| self.insert(*pair) }
  end

  def insert(sentence, time = 1)
    @h[sentence] += time

    time = @h[sentence]
    curr = @root

    sentence.each_char do |ch|
      if ch == '#'
        curr[ch] = {val: sentence[0...-1], max: time }
        return
      end

      curr[ch] ||= {max: 0}

      curr[ch][:max] = time if time > curr[ch][:max]

      curr = curr[ch]
    end
  end

  def input(ch)
    @sentence += ch

    if ch == '#'
      self.insert(@sentence, 1)
      @sentence = ''
      @curr = @root
      return []
    end

    @curr = @curr[ch]
    
    return [] unless @curr
    
    queue = [@curr]
    res = []

    until queue.empty?
      node = queue.shift

      if (node[:val])
        res << node[:val]
        next
      end
      
      node.each_key do |ch|
        next if ch == :max

        child = node[ch]
        
        (0..2).each do |i|
          if queue[i].nil? || child[:max] > queue[i][:max]
            queue = queue[0...i] + [child] + queue[i...2] 
            break
          end
        end

      end
    end

    res
  end
end

a = AutocompleteSystem.new(["i love a#", "i love b#", "i love c#", "i love d#"], [5,5,5,5]);
p a.input('i')
p a.input(' ')
p a.input('a')
p a.input('#')
p a.input('i')
p a.input(' ')
p a.input('a')
p a.input('#')