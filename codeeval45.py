#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.07.29

# From http://www.codeeval.com/public_sc/45/ -- "The problem is as
# follows: choose a number, reverse its digits and add it to the
# original. If the sum is not a palindrome (which means, it is not the
# same number from left to right and right to left), repeat this
# procedure."

import sys

lines = open(sys.argv[1], 'r').readlines()
lines = [int(line) for line in lines] # Convert strings to ints

# Takes an int, returns its 'reverse'
reverse = lambda num: int( str(num)[::-1] )

for num in lines:
    times = 0
    while num != reverse(num):
        num   += reverse(num)
        times += 1
    print times, num
