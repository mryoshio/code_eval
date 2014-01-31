File.open(ARGV[0]) do |f|
  f.each_line do |l|
    a,b = l.split(",").map {|v| v.to_i }
    puts a - a/b * b
  end
end
