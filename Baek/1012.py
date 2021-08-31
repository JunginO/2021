t=int(input())

for _ in range(t):
    olist=[]
    m,n,k=map(int, input().split())
    for i in range(k):
        ilist=[]
        tmp1,tmp2=map(int,input().split())
        ilist.append(tmp1)
        ilist.append(tmp2)
        olist.append(ilist)
    olist.sort()
