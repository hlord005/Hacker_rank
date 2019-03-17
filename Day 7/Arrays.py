if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for i in range(n):
        p = arr.pop()
        print(p, end=' ')
