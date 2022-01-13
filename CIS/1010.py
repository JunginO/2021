n,maxweight=map(int,input().split())
pl=[]
wl=[]
for _ in range(n):
    price,weight=map(int,input().split())
    pl.append(price)
    wl.append(weight)
lst=[[0 for i in range(maxweight+1)]for j in range(n+1)]
for i in range(n+1):
    for j in range(maxweight+1):
        if i==0 or j==0:
            lst[i][j]=0
        elif wl[i-1]<=j:
#knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
            lst[i][j]=max(pl[i-1]+lst[i-1][j-wl[i-1]],lst[i-1][j])
        else:
            lst[i][j]=lst[i-1][j]
print(lst[n][maxweight])