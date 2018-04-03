# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 19:46:32 2018

@author: yuwan
"""

import sys

bignum = 1000000007

d = [1]
for i in range(1, 10000):
    d.append((d[i-1]*2) % bignum)


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        num = int(sys.stdin.readline())
        l = [int(n) for n in sys.stdin.readline().split()]
        ans = encode(num, l)
        sys.stdout.write('Case #{}: {}\n'.format(case+1, ans))


def encode(num, l):
    out = 0
    diffs = [a-b for a,b in zip(l[1:],l)]
    prevdiff = 0
    for i in range(num/2):
        mult = prevdiff + sum(d[i:(num-1-i)]) % bignum
        mult2 = diffs[i] + diffs[num-2-i] if i != num-2-i else diffs[i]
        out = int((out+mult*mult2)% bignum)
        prevdiff = mult
    return out
            
if __name__ == '__main__':
    main()