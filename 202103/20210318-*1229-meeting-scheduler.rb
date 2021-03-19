def firstInterval(s1, s2, d)
  curr = nil

  (s1 + s2)
    .sort{|a, b| a[0] <=> b[0]}
    .each do |interval|
      unless curr
        curr = interval
        next
      end

      start, e = interval

      return [start, start + d] if (start + d) <= [e, curr[1]].min

      curr = interval if (e > curr[1])
    end

  []
end

p firstInterval([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12)