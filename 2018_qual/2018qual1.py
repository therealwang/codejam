# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from collections import defaultdict

def universe(d, command):
    ind = 0
    totmap = defaultdict(lambda: 0)
    tot = 0
    for letter in command:
        if letter == 'C':
            ind += 1
        else:
            totmap[ind] += 1
            tot += 1 << ind
    
    if sum(totmap.values()) > d:
        return 'IMPOSSIBLE'
    else:
        out = 0
        currmax = ind
        while tot > d:
            while totmap[currmax] > 0 and tot > d:
                totmap[currmax] -= 1
                totmap[currmax - 1] += 1
                tot -= 1 << (currmax - 1)
                out += 1
            currmax -= 1
        return out

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        d, command = sys.stdin.readline().split()
        d = int(d)
        ans = universe(d, command)
        print 'Case #{}: {}'.format(case + 1, ans)
        
main()
