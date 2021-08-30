n,k=map(int,input().split())
lst=[]
total=0

for i in range(n):
    tmp=int(input())
    lst.append(tmp)
while n>=0:
    if k//lst[n-1]==0:
       n-=1
    else:
        total+=(k//lst[n-1])
        k%=lst[n-1]
        n-=1
        
print(total)