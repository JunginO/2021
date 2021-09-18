 
n=int(input())
A = list(map(int, input().split()))
A.sort()
m=int(input())
M = list(map(int, input().split()))

def searcher(i,A,start,end):
    if start > end:
        return False
    m=(start+end)//2

    if i==A[m]:
        return True
    elif i<A[m]:
        return searcher(i,A,start,m-1)
    else:
        return searcher(i,A,m+1,end)
end=len(A)-1
for i in M:
    if searcher(i,A,0,end):
        print(1)
    else:
        print(0)


