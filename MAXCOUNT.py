#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.02.01

# From http://www.codechef.com/FEB12/problems/MAXCOUNT

# "First line of input contains an integer T, denoting the number of
# test cases"
for _ in range(int(raw_input())):
    # "Each case begins with a single integer N, the length of [array] A"
    N = int(raw_input()) # Not used

    # "Then follows N space separated integers"
    # (That is, len(numbers) == N)
    numbers = sorted([int(x) for x in raw_input().split()], reverse=True)

    # "...for all i in [1..N] : 1 <= A[i] <= 10000"
    # (That is, `value`'s maximum value is 10000)
    value, count = 10001, -1

    # (For each unique number in `numbers`, store the most frequently
    # occurring number in `value` and its count in `count`)
    for this_value in sorted(list(set(numbers)), reverse=True):
        this_count = numbers.count(this_value)
        # "In case of ties, choose the smaller element first."
        # (Save smallest number that occurs the most number of times.
        # We'll get the smallest in case of a tie because we're
        # iterating through the numbers in reverse-sorted order.)
        if this_count >= count:
            value, count = this_value, this_count

    # "For each test case, output two space separated integers V &
    # C. V is the value which occurs maximum number of times and C is
    # its count.
    print value, count
