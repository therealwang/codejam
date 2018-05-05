# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:28:09 2018

@author: yuwan
"""

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
        d = defaultdict(lambda: defaultdict(lambda: 0))
        out = [1]
        d[0][(mns[0][0],INF)] += 1
        d[0][(INF,mns[0][1])] += 1
        for i in range(1, numsigns):
            d[i][(mns[i][0],INF)] += 1
            d[i][(INF,mns[i][1])] += 1
            for k in d[i-1]:
                if k[0] == INF:
                    d[i][(mns[i][0],k[1])] = max(d[i-1][k] + 1, d[i][(mns[i][0],k[1])])
                if k[1] == INF:
                    d[i][(k[0],mns[i][1])] = max(d[i-1][k] + 1, d[i][(k[0],mns[i][1])])
                if k[1] == mns[i][1] or k[0] == mns[i][0]:
                    d[i][k] = max(d[i-1][k]+1,d[i][k])
                    
        out = [max(d[i].values()) for i in d]
        maxv = max(out)
        c = out.count(maxv)
        print "Case #{}: {} {}".format(case+1, maxv, c)
        
main()
        