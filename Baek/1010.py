t=int(input())
def calc(x):
    tmp=1
    for i in range(1,x+1):
        tmp*=i
    return tmp
    

for _ in range(t):
    n,m=map(int,input().split())
    ans=calc(m)/((calc(m-n)*calc(n)))
    print(int(ans))