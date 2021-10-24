import sys
n=int(sys.stdin.readline())
lst=[list(map(int, sys.stdin.readline().split())) for i in range(n)]

lst.sort()
ans=[lst[0]]
machine=1
for i in range(1,n):
    for k in range(len(ans)):
        if ans[k][1]>lst[i][0]:
            cng=True
        else:
            ans[k]=lst[i]
            cng=False
            break
    if cng:
        machine+=1
        ans.append(lst[i])     
print(machine)
