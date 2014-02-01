File.open(ARGV[0]) do |f|
  f.each_line do |l|
    ll = l.chomp.split("")
    puts (l.to_i == ll.map {|v| v.to_i ** ll.size }.inject {|sum, v| sum + v }) ? "True" : "False"
  end
end
