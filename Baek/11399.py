n=int(input())
lst=list(map(int, input().split()))
totalt=0
lst.sort()
for i in range(n):
    for j in range(i+1):
        totalt+=lst[j]
print(totalt)