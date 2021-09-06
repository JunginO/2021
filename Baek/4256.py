t=int(input())
for _ in range(t):
    n=int(input())
    preord=list(map(int,input().split()))
    inord=list(map(int,input().split()))
    postord(preord,inord)
