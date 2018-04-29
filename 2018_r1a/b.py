# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:48:23 2018

@author: yuwan
"""


import sys
import operator


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        r, b, c = [int(a) for a  in sys.stdin.readline().split()]

        cashiers = []
        for _ in range(c):
            m, s, p = [int(a) for a in sys.stdin.readline().split()]
            cashiers.append((m,s,p))
            
        out = bits(r,b,cashiers)
        print 'Case #{}: {}'.format(case+1, out)
        
        
def bits(r,b,cashiers):
    ul = max([min(b,m)*s+p for m,s,p in cashiers])
    ll = 0
    mid = (ul+ll+1)/2
    
    d, totbits = findtot(r,cashiers,mid)
    
    broken = False
    while totbits != b:
        if ul <= ll:
            broken = True
            break
        if totbits > b:
            ul = mid - 1
            mid = (1+ul+ll)/2
            d, totbits = findtot(r,cashiers,mid)
            tempd = d
        else:
            ll = mid
            mid = (1+ul+ll)/2
            d, totbits = findtot(r,cashiers,mid)
        totbits = totbits
        
    if broken:
        d = tempd
        
    sl = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
    
    print sl
    
    maxv = 0
    for i in range(r):
        cashier = sl[i][0]
        bits = sl[i][1]
        maxv = max(maxv, cashier[1]*bits + cashier[2])
        
    return maxv
    
    

def findtot(r, cashiers, mid):
    d = {}
    for c in cashiers:
        d[c] = min((mid-c[2])/c[1],c[0])
        
    return d, sum(sorted(d.values(),reverse = True)[:r])
    
main()