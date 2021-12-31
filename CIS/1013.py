n=int(input())
lst=[]
for _ in range(n):
    si,fi=map(int,input().split())
    lst.append([si,fi])
lst.sort(key=lambda x:x[1])
ans=[]

for i in range(n):
    if i==0:
        ans.append(lst[0])
    else:
        if ans[-1][1]<=lst[i][0]:
            ans.append(lst[i])
print(len(ans))
