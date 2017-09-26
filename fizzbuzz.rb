#!/usr/bin/env ruby

(1..100).each do |num|
  three = (num % 3 == 0)
  five = (num % 5 == 0)
  print 'fizz' if three
  print 'buzz' if five
  print num if (!three and !five)
  puts
end
