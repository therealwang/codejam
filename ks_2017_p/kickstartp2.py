from __future__ import division
import sys


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        n, m = [int(n) for n in sys.stdin.readline().split()]
        tot = n + m
        orignum = tot - 2*m
        origden = tot
        print 'Case #{}: {:.8f}'.format(case + 1, orignum/origden)

main()
