require 'kramdown'
require 'rouge'
require 'kramdown-math-katex'
require 'kramdown-parser-gfm'
fname = ARGV[0]
fcontents = File.read(fname)
res = Kramdown::Document.new(fcontents, {input: 'GFM',math_engine: "katex",syntax_highlighter: "rouge"}).to_html
puts res
