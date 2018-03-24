# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:57:26 2018

@author: yuwan
"""

def main_small():
    cases = int(raw_input())
    for case in range(1, cases+1):
        K = [int(a) for a in raw_input().split()][0]
        ans = ''.join([str(a)+' ' for a in range(1,K+1)])[:-1]
        print 'Case #{}: {}'.format(case, ans)
        
main_small()