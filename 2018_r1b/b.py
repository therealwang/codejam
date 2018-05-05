# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:51:50 2018

@author: yuwan
"""


import sys
from collections import defaultdict

INF = 1 << 32

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        numsigns = int(sys.stdin.readline())
        signs = []
        for _ in range(numsigns):
            signs.append([int(a) for a in sys.stdin.readline().split()])
        mns = [(s[0]+s[1], s[0]-s[2]) for s in signs]
        out = [(1, INF, INF)]
        for i in range(1, numsigns):
            if len(out[i-1] == 2):
            else:
                if mns[i][0] == mns[i-1][0] == out[i-1][1]:
                    out.append((out[i-1][0]+1, out[i-1][1], out[i-1][2]))  
                elif mns[i][1] == mns[i-1][1] == out[i-1][2]:
                    out.append((out[i-1][0]+1, out[i-1][1], out[i-1][2])) 
                elif mns[i][0] == mns[i-1][0] and out[i-1][1] == INF:
                    out.append((out[i-1][0]+1, mns[i][0], out[i-1][2]))  
                elif mns[i][1] == mns[i-1][1] and out[i-1][2] == INF: 
                    out.append((out[i-1][0]+1, out[i-1][1], mns[i][1])) 
                elif out[i-1][1] == out[i-1][2] == INF:
                    out.append((out[i-1][0]+1, INF))
                elif out[i-1][1] == INF:
                    out.append((out[i-1][0]+1, mns[i][0], out[i-1][2]))
                elif out[i-1][2] == INF:
                    out.append((out[i-1][0]+1, out[i-1][1], mns[i][1])) 
                else:
                    out.append((1, INF, INF))
            
        print mns        
        print out
        out = [o[0] for o in out]
        maxv = max(out)
        c = out.count(maxv)
        print "Case #{}: {} {}".format(case+1, maxv, c)
        
main()
        