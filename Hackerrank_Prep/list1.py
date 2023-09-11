'''
Created on Aug 2, 2023

@author: shanti
'''
def handle(l, comm, *args):
    try:
        getattr(l, comm)(*args)
    except AttributeError:
        if comm == 'print':
            exec("print(l)")
    return l
def main():
    l = []
    N = int(input())
    for _ in range(0,N):
        comm, *args = input().split()
        args = list(map(int, args))
        l = handle(l, comm, *args)
if __name__ == '__main__':
    main()