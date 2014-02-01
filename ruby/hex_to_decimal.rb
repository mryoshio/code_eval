File.open(ARGV[0]) do |f|
  f.each_line do |l|
    puts l.hex
  end
end
