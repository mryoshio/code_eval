b = Array.new(257).map{[0, 0]}
h = {
  "SetCol" => 0,
  "SetRow" => 1,
  "QueryCol" => 0,
  "QueryRow" => 1
}

=begin
File.open(ARGV[0]) do |f|
  f.each_line do |l|
    d, k, v = l.split(/\s/)
    case d
    when /^Set/
      b[k.to_i][h[d]] = v.to_i
    when /^Query/
      puts b.inject(0) {|sum, a| sum += a[h[d]] }
    end
  end
end
=end

rows = {}
cols= {}

File.open(ARGV[0]) do |f|
  f.each_line do |l|
    d, k, v = l.split(/\s/)
    case d
    when /^SetCol/
      cols[k.to_i] = v.to_i
    when /^SetRow/
      rows[k.to_i] = v.to_i
    when /^QueryCol/
      default = cols[k.to_i].to_i
      rows
    when /^QueryRow/
      default = rows[k.to_i].to_i
    end
  end
end
