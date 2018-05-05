# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:34:36 2018

@author: yuwan
"""

import random

f = open('test.txt', 'w')

f.write('100\n')

for i in range(100):
    n = random.randint(2,25)
    l = random.randint(1, n-1)
    f.write('{} {}\n'.format(n, l))
    f.write(('1 '*l)[:-1]+'\n')

f.close()


f = open('test2.txt', 'w')

f.write('3\n')

for i in range(3):
    f.write('10000\n')
    for i in range(10000):
        f.write('{} {} {}\n'.format(random.randint(1, 1e5),random.randint(1, 1e5),random.randint(1, 1e5)))


f.close()