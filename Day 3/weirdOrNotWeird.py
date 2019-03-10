#!/bin/python3

if __name__ == '__main__':
    N = int(input())
    if N >= 1 and N <= 100:
        if N % 2 == 0:
            if N in [2, 4] or N > 20:
                print('Not Weird')
            elif N >= 6 and N <= 20:
                print('Weird')
        else:
            print('Weird')
