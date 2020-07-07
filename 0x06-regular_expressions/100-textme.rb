#!/usr/bin/env ruby
sender = ARGV[0][/from:([^\s\]]+)/, 1]
receiver = ARGV[0][/to:([^\s\]]+)/, 1]
flags = ARGV[0][/flags:([^\s\]]+)/, 1]
puts "#{sender},#{receiver},#{flags}"
