# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:04:03 2018

@author: yuwan
"""

from __future__ import division
import sys

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        dest, horses = [int(n) for n in sys.stdin.readline().split()]
        slowest = -1
        for horse in range(horses):
            loc, speed = [int(n) for n in sys.stdin.readline().split()]
            slowest = max(slowest, (dest-loc)/speed)
        print 'Case #{}: {:.6f}'.format(case + 1, dest/slowest)
        
        
main()