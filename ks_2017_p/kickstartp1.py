import sys
from collections import Counter

def main():
    cases = int(sys.stdin.readline())
    
    for case in range(cases):
        d = dict()
        names = int(sys.stdin.readline())
        for _ in range(names):
            name = sys.stdin.readline().strip()
            tempcounter = Counter(name)
            d[name] = len(tempcounter) if ' ' not in tempcounter else len(tempcounter) - 1
        maxv = max(d.values())
        maxunique = [k for k in d if d[k] == maxv]
        sys.stdout.write('Case #{}: {}\n'.format(case + 1, min(maxunique)))


main()
        
