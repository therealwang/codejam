# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 17:31:41 2018

@author: yuwan
"""

import sys


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        N, K = [int(a) for a in sys.stdin.readline().split()]
        tempk = K
        power = 0
        while tempk > 0:
            tempk /= 2
            power += 1
        remainder = K % (1 << power - 1)
        first = N /  (1 << power)
        hasReached = N % (1 << power - 1)
        if N%(1 << power) >= 1 << (power - 1):
            second = first
        else:
            second = first - 1
        if hasReached < remainder:
            first = first - 1
        minn, maxn = min(first, second), max(first, second)
        print "Case #{}: {} {}".format(case + 1, maxn, minn)
  
        
main()