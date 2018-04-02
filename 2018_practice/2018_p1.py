# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:14:49 2018

@author: yuwan
"""

import sys

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        nextline = sys.stdin.readline()
        a,b = [int(n) for n in nextline.split()]
        n = int(sys.stdin.readline())
        response = ''
        while response != 'CORRECT':
            guess = (1+a+b)/2
            sys.stdout.write(str(guess)+'\n')
            sys.stdout.flush()
            response = sys.stdin.readline().strip()
            if response == 'TOO_SMALL':
                a = guess
            elif response == 'TOO_BIG':
                b = guess - 1
            else:
                break

main()

