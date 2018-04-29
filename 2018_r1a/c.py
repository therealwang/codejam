# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:59:45 2018

@author: yuwan
"""

import sys
import math

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        n, p = [int(a) for a  in sys.stdin.readline().split()]
        
        currp = 0
        cuts = []
        for _ in range(n):
            w, h = [int(a) for a in sys.stdin.readline().split()]
            currp += 2*(w+h)
            mincut = min(w,h)
            maxcut = math.sqrt(w**2+h**2)
            cuts.append((mincut, maxcut))
            
        out = cookie(cuts, p, currp)
        print 'Case #{}: {:.8f}'.format(case+1, out)
        
        
        
def cookie(cuts, p, currp):
    desiredcut = p - currp
    desiredcut = float(desiredcut)/2
    totalmin = sum([c[0] for c in cuts])
    totalmax = sum([c[1] for c in cuts])
        
    if desiredcut > totalmin:
        return min(2*totalmax+currp, p)
    
    minval = cuts[0][0]
    maxval = cuts[0][1]
    
    cutlen = 0
    for i in range(1,len(cuts)+1):
        if i*minval > desiredcut:
            cutlen = min(desiredcut,(i-1)*maxval)
            break
        elif i*minval <= desiredcut <= i*maxval:
            cutlen = desiredcut
            break
        
    return 2*(cutlen) + currp

main()