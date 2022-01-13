n=int(input())

lst = [[0] * (n) for _ in range(n+1)]

for i in range(n):
    tmp= list(map(int, input().split()))
    for j in range(n):
        lst[i][j]=tmp[j]

for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

for i in range(0, n):
    for j in range(0, n):
            print(lst[i][j], end=' ')
    print()