t=File.open(ARGV.first).read.split
puts t.reverse.join " "
puts t.map{|w| w.reverse}.join " "
