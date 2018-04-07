# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 23:28:42 2018

@author: yuwan
"""

import sys
import math

def findcomplement(angle):
    newl = math.sin(angle)*math.sqrt(2)/2
    newanticos = math.sqrt(newl**2 + 0.5)
    return math.acos(newanticos)

def findub():
    lb = 0
    ub = math.pi/2
    test = (lb+ub)/2
    while abs(test - findcomplement(test)) >= 1e-7:
        if test > findcomplement(test):
            ub = test
        else:
            lb = test
        test = (lb+ub)/2
    return test

compub = findub()

def binsearch(targ):
    lb = 0
    ub = math.pi/4
    test = (lb + ub)/2
    while abs(math.cos(test)+math.sin(test) - targ) >= 1e-6:
        if math.cos(test)+math.sin(test) > targ:
            ub = test
        else:
            lb = test
        test = (lb+ub)/2
    return test

def binsearch2(targ):
    lb = 0
    ub = compub
    test = (lb+ub)/2
    while abs(math.sin(test)+ 2*math.sin(findcomplement(test)) - targ) >= 1e-6:
        if math.sin(test)+ 2*math.sin(findcomplement(test)) > targ:
            ub = test
        else:
            lb = test
        test = (lb+ub)/2
        
    return test

def findrotation(targ):
    if targ <= 1.414213:
        rad = binsearch(targ)
        a = (math.sin(rad)/2, math.cos(rad)/2,0)
        b = (-math.cos(rad)/2, math.sin(rad)/2,0)
        c = (0, 0, 0.5)
        return a,b,c
    else:
        rad = binsearch2(targ)
        a = (math.sqrt(2)/4,math.cos(rad)*math.sqrt(2)/4,-math.sin(rad)*math.sqrt(2)/4)
        b = (-math.sqrt(2)/4,math.cos(rad)*math.sqrt(2)/4,-math.sin(rad)*math.sqrt(2)/4)
        c = (0, math.sin(rad)/2, math.cos(rad)/2)
        return a,b,c
    


    
def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        targ = float(sys.stdin.readline())
        out = findrotation(targ)
        print 'Case #{}:'.format(case+1)
        for point in out:
            print ' '.join([str(value) for value in point])
        
main()
'''
def dist(point):
    out = 0
    for i in point:
        out += i**2
    return math.sqrt(out)


def test(targ):
    a,b,c = findrotation(targ)
    for p in [a,b,c]:
        print 'Distance to {}: {}'.format(p, dist(p))
        
    for i,j in [(a,b),(a,c),(b,c)]:
        print 'angles: {}'.format(np.dot(i,j))
        
    area = 0
    for p in [a,b,c]:
        area += p[1]
    print 'area: {} vs {}'.format(targ, area*2)
'''