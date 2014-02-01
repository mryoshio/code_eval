alphas = 'a'..'z'
org = {}
alphas.each { |s| org[s] = 0 }

File.open(ARGV[0]) do |f|
  f.each_line do |l|
    ll = l.chomp.split('').map {|v| v.downcase }
    h = org.dup
    ll.each { |v| h[v] += 1 if alphas.include?(v) }
    sum = 0
    h.sort_by { |k, v| v }.reverse.each_with_index do |(k, v), i|
      sum += v*(26-i)
    end
    puts sum
  end
end
