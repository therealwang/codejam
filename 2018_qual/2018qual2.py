# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 20:20:57 2018

@author: yuwan
"""
import sys

def checktrouble(n,l):
    slice1 = range(0, n, 2)
    slice2 = range(1, n, 2)
    l1 = [l[i] for i in slice1]
    l2 = [l[i] for i in slice2]
    l1.sort()
    l2.sort()
    for i in range(n-1):
        if i % 2 == 0 and l1[i/2] > l2[i/2]:
            return i
        elif i % 2 == 1 and l2[i/2] > l1[i/2 + 1]:
            return i
    return 'OK'
    
    
def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        n = int(sys.stdin.readline())
        l = [int(a) for a in sys.stdin.readline().split()]
        cond = checktrouble(n, l)
        print 'Case #{}: {}'.format(case+1, cond)
        
if __name__ == '__main__':        
    main()