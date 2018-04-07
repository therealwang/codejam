# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 23:28:42 2018

@author: yuwan
"""

import sys
import math

f = open('test.txt','w')

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        area = int(sys.stdin.readline())
        w = int(math.sqrt(area))
        l = w + 1
        print('500 500')
        sys.stdout.flush()
        i, j = [int(a) for a in sys.stdin.readline().split()]
        d = dict()
        for x in range(1, w - 1):
            for y in range(1, l-1):
                d[(i+x,j+y)] = 9
        filled = set((i,j))
        while i != 0 and j != 0:
            maxv = max(d.values())
            templ = [k for k in d if d[k] == maxv]
            print(' '.join([str(a) for a in templ[0]]))
            f.write(str(templ[0]) + ' ' +  str((i,j)) +' ' + str(d) +'\n')
            sys.stdout.flush()
            try:
                i,j = [int(a) for a in sys.stdin.readline().split()]
            except:
                return
            if i == -1 and j == -1:
                return
            if (i,j) not in filled:
                filled.add((i,j))
                for d1 in [-1,0,1]:
                    for d2 in [-1,0,1]:
                        if (i+d1,j+d2) in d:
                            d[(i+d1,j+d2)] -= 1
            
            
main()