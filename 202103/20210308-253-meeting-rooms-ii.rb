def intervals
    q = []
    ct = 0
    max = 0

    intervals.each {|interval| q.push(interval.start, -interval.end) }

    q.sort!{|a, b| a.abs - b.abs }

    q.each do |el|
        ct += el > 0 ? 1 : -1
        max = ct if ct > max
    end

    max
end