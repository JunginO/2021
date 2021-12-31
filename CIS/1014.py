import math
n,k=map(int,input().split())
dots=[]
for _ in range(n):
    x,y=map(int,input().split())
    dots.append([x,y])
def dist(p1, p2):
    tmp=((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return math.sqrt(tmp)
C=[]
ans=[0]
C.append(dots[0])
for j in range(1,k):
    D=[99999 for i in range(0,n)]
    for i in range(0,n):
        if dots[i] in C:
            D[i]=0
        else:
            for l in range(len(C)):
                D[i]=min(dist(dots[i],C[l]),D[i])   
    C.append(dots[D.index(max(D))])
    ans.append(D.index(max(D)))
ans.sort()
for i in ans:
    print(dots[i][0], dots[i][1])
        