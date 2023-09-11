'''
Created on Jul 2, 2023

@author: shanti
'''
import numpy as np

if __name__ == '__main__':
    arr1 = input().strip().split()
    arr2 = np.array(arr1, int).reshape(3,3)
    print(arr2)