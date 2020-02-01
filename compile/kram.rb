require 'kramdown'
require 'rouge'
require 'kramdown-math-katex'
fname = ARGV[0]
fcontents = File.read(fname)
res = Kramdown::Document.new(fcontents, {math_engine: "katex",syntax_highlighter: "rouge"}).to_html
puts res
