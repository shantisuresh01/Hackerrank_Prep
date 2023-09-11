'''
Created on Aug 2, 2023

@author: shanti
'''

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))