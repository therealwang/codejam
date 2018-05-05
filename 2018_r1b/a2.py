# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:53:12 2018

@author: yuwan
"""


import sys
import math

INF = 1 << 32


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        n, l = [int(a) for a in sys.stdin.readline().split()]
        inc = (100./n) % 1
        votes = [float(a) for a in sys.stdin.readline().split()]
        remaining = int(n - sum(votes))
        dec = [a/n*100 % 1 for a in votes]
        dec = [-INF if a >= 0.5 else a for a in dec]
        if inc == 0:
            print "Case #{}: 100".format(case+1)
        else:
            dec = [math.ceil((0.5-a)/inc) for a in dec]
            mininc = math.ceil(0.5/inc)
            while remaining >= min(dec):
                minval = min(dec)
                remaining -= minval
                ind = dec.index(minval)
                votes[ind] += minval
                dec[ind] = (votes[ind]/n*100) % 1
                dec[ind] = -INF if dec[ind] >= 0.5 else dec[ind]
                dec[ind] = math.ceil((0.5-dec[ind])/inc)
                    
            if remaining:
                nummins = int(remaining/mininc)
                remaining -= mininc * nummins
                votes += [mininc]*nummins
                votes += [remaining]
            votes = [round(vote*100./n) for vote in votes]
            
            print "Case #{}: {}".format(case+1, int(sum(votes)))
            
            
                    
        
main()