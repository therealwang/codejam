# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:53:53 2018

@author: yuwan
"""
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        parties  = int(sys.stdin.readline())
        senators = [int(a) for a in sys.stdin.readline().split()]
        out = ''
        while sum(senators) > 0:
            maxsens = max(senators)
            ismax = [i for i in range(parties) if senators[i] == maxsens]
            if sum(senators) == 3:
                out += alphabet[ismax[0]] + ' '
                senators[ismax[0]] -= 1
            else:
                if len(ismax) > 1:
                    out += alphabet[ismax[0]] + alphabet[ismax[1]] +  ' '
                    senators[ismax[0]] -= 1
                    senators[ismax[1]] -= 1
                else:
                    out += alphabet[ismax[0]]* 2 + ' '
                    senators[ismax[0]] -= 2
                
        print 'Case #{}: {}'.format(case+1, out.strip())
main()