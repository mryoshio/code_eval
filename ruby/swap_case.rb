File.open(ARGV[0]) do |f|
  f.each_line { |l| l.each_char { |c| print c.swapcase } }
end
