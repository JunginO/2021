k,n=map(int,input().split())
a=[]

for _ in range(k):
    a.append(int(input()))
low=1
high=sum(a)//n
while low<=high:
    mid=(low+high)//2
    cnt=0
    for i in range(k):
        cnt+=a[i]//mid
    if cnt<n:
        high=mid-1   
    else:
        low=mid+1  
print(high)

