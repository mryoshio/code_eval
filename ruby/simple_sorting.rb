File.open(ARGV[0]) do |f|
  f.each_line do |l|
    puts l.chomp.split(' ').map{ |v| v.to_f }.sort.join(' ')
  end
end
