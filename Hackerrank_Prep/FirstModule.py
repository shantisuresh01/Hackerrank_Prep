'''
Created on Jun 29, 2023

@author: shanti
'''
def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b

if __name__ == '__main__':
    print(add(6,6))