# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 20:58:42 2018

@author: yuwan
"""

import sys
import re

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        r, c, h, v = [int(a) for a in sys.stdin.readline().split()]
        rowdict = {i: 0 for i in range(r)}
        coldict = {i: 0 for i in range(c)}
        rowcoldict = {}
        for i in range(r):
            nextline = sys.stdin.readline()
            rowdict[i] = nextline.count('@')
            cols = [m.start() for m in re.finditer('@',nextline)]
            for col in cols:
                coldict[col] += 1
            if i == 0:
                for colind in range(c):
                    if colind in cols:
                        rowcoldict[(0,colind)] = 1
                    else:
                        rowcoldict[(0,colind)] = 0
            else:
                for colind in range(c):
                    if colind in cols:
                        rowcoldict[(i,colind)] = rowcoldict[(i-1,colind)] + 1
                    else:
                        rowcoldict[(i,colind)] = rowcoldict[(i-1,colind)]
        
        out = testpancake(rowdict, coldict, rowcoldict, h, v, c)
        print 'Case #{}: {}'.format(case + 1, out)
        

        
def testpancake(rowdict, coldict, rowcoldict, h, v, c):
    total_chips = sum(rowdict.values()) 
    if total_chips % ((h+1)*(v+1)) != 0:
        return 'IMPOSSIBLE'
    
    row_n = total_chips / (h+1)
    col_n = total_chips / (v+1)
    
    each_n = total_chips / ((h+1)*(v+1))
    
    currchips = 0
    rowcuts = []
    colcuts = []
    
    for i in range(len(rowdict)):
        currchips += rowdict[i]
        if currchips > row_n:
            return 'IMPOSSIBLE'
        elif currchips == row_n:
            currchips = 0
            rowcuts.append(i)
            
    for i in range(c):
        currchips += coldict[i]
        if currchips > col_n:
            return 'IMPOSSIBLE'
        elif currchips == col_n:
            currchips = 0
            colcuts.append(i)
            
    colcuts = [0] + [temp + 1 for temp in colcuts]        
    for initcol, endcol in zip(colcuts, colcuts[1:]):
        mult = 1
        for row in rowcuts:
            tot = sum([rowcoldict[(row, col)] for col in range(initcol, endcol)])
            if tot != mult * each_n:
                return 'IMPOSSIBLE'
            mult += 1
            
    

            
    return 'POSSIBLE'

main()
    
        