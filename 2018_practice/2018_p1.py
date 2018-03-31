# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:14:49 2018

@author: yuwan
"""

import sys

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        a,b = [int(n) for n in sys.stdin.readline().split()]
        response = ''
        while response != 'CORRECT':
            return
            guess = 1+ (b-a)/2+a
            sys.stdout.write(str(guess))
            sys.stdout.flush()
            response = sys.stdin.readline().strip()
            if response == 'TOO_SMALL':
                a = guess
            if response == 'TOO_BIG':
                b = guess - 1
            if response == 'WRONG_ANSWER':
                break
            
main()