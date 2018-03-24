# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:57:26 2018

@author: yuwan
"""

def main():
    cases = int(raw_input())
    for case in range(1, cases+1):
        K,C,S = [int(a) for a in raw_input().split()]
        if S < K+1-C:
            print 'Case #{}: IMPOSSIBLE'.format(case)
        else:
            init = 0
            for i in range(min(C-1,K-1)):
                init += i * K**i
            ans = ''.join([str(a)+' ' for a in range(init + min(C,K),init + K+1)])[:-1]
            print 'Case #{}: {}'.format(case, ans)
        
main()