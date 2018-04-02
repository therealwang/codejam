import sys


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        l, r = [int(n) for n in sys.stdin.readline().split()]
        num = min(l,r)
        print 'Case #{}: {}'.format(case + 1, num*(num+1)/2)

main()
