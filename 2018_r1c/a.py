# -*- coding: utf-8 -*-
"""
Created on Sat May 05 04:57:27 2018

@author: yuwan
"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import sys
from collections import defaultdict
from operator import mul

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        n, l = [int(a) for a in sys.stdin.readline().split()]
        suffixes = []
        letters = []
        for i in range(l):
            suffixes.append(defaultdict(lambda: 0))
            letters.append(set())
        for _ in range(n):
            word = sys.stdin.readline().strip()
            for i in range(l):
                suffixes[i][word[i:]] += 1
                letters[i].add(word[i])
        
        print 'Case #{}: {}'.format(case+1, newword(l,suffixes,letters))
                
        
            
        
            
            
            
            
def newword(l, suffixes, letters):
    lettercount = [len(s) for s in letters]
    wordspossible = [reduce(mul, lettercount[:i+1], 1) for i in range(l)]
    
    cand = ''
    for i in reversed(range(l)):
        templ = [c + cand for c in letters[i]]
        tempd = {c: suffixes[i][c] for c in templ}
        cand = min(tempd, key = tempd.get)
        if i > 0:
            if suffixes[i][cand] == wordspossible[i-1]:
                return '-'
        else:
            if suffixes[i][cand] == 0:
                return cand
            else:
                return '-'
            
testlist = [a+b for a in letters for b in letters] 

def test(n=4):
    testlist = ['AA','BA','AB','BB']
    l = 2
    for tempn in range(1,n+1):
        suffixes = []
        letters = []
        for i in range(l):
            suffixes.append(defaultdict(lambda: 0))
            letters.append(set())
        for case in range(tempn):
            word = testlist[case]
            for i in range(l):
                suffixes[i][word[i:]] += 1
                letters[i].add(word[i])
                
        print testlist[:tempn]
        print newword(l, suffixes, letters)
    #main()
    
main()