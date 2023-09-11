'''
Created on Jul 1, 2023

@author: shanti
'''
from itertools import groupby
if __name__ == '__main__':
    s = input()
    groups = groupby(s)
    for key, group in groups:
        print(f"({len(list(group))}, {key})", end=' ')
    print()
