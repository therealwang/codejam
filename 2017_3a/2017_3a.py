# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:44:40 2018

@author: yuwan
"""

from collections import defaultdict, deque
from numpy import math
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def multichoose(string):
    tot = sum([int(a) for a in string])
    resid = len(string) - tot
    out = math.factorial(len(string))/prod([math.factorial(int(a)) for a in string])
    if string == '1' + '0' * (len(string)-1):
        return out/math.factorial(resid) - 1
    return out/math.factorial(resid) if resid >= 0 else 0

def findsumton(length, tot, initlen, out = ''):
    output = []
    if length == 1:
        tempout = [0] * (initlen+1)
        for s in out + str(tot):
            tempout[int(s)] += 1
        pred = ''.join([str(a) for a in tempout[1:]])
        return [(out+str(tot), pred)]
            
    else:
        for i in range(0, 10):
            if i <= tot:
                output += findsumton(length -1, tot-i, initlen, out + str(i))
            
    return output

def allpossible(length):
    out = []
    for i in range(1,length+1):
        out += findsumton(length, i, length)
    return out

class Graph:
    def __init__(self, allposs):
        self.edges = defaultdict(set)
        for out, pred in allposs:
            self.edges[pred].add(out)
        
        inv =  '1' + '0'*(len(allposs[0][0])-1)
        self.edges[inv].remove(inv)
            
        
def findnumpreds(num):
    l = allpossdict[len(num)]
    g = Graph(l)
    
    out = 1 + multichoose(num)
    q = deque(g.edges[num])
    visited = set()
    
    while q:
        n = q.pop()
        visited.add(n)
        out += multichoose(n)
        q.extend([k for k in g.edges[n] if k not in visited])
            
        
    
    return out

allpossdict = {i: allpossible(i) for i in range(1,10)}

def main():
    n = int(raw_input())
    for i in range(1,n+1):
        out = findnumpreds(raw_input())
        print 'Case #{}: {}'.format(i, out)
        
main()