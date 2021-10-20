import sys

def quick_sort(lst):
    if len(lst) <=1:
        return lst
    key=lst[0]
    sml_lst,eql_lst,big_lst=[],[],[]
    for i in lst:
        if i<key:
            sml_lst.append(i)
        elif i>key:
            big_lst.append(i)
        else:
            eql_lst.append(i)
    return quick_sort(sml_lst)+eql_lst+quick_sort(big_lst)


#특정 원소가 속한 집합을 찾는다
def find(parent, x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합을 합친다(간선 연결이라고 생각)
def union(parent, x,y):
    x=find(parent,x)
    y=find(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

n,m=map(int,sys.stdin.readline().split())
#parent 초기화 및 셀프 루트노드 설정
parent=[0]*(m+1)
for i in range(1,n+1):
    parent[i]=i
lst=[]
for _ in range(m):
    x,y,w=map(int,sys.stdin.readline().split())
    lst.append([w,x,y])

ans=0
for i in quick_sort(lst):
    w,x,y=i[0],i[1],i[2]
    if find(parent,x)!=find(parent,y):
        union(parent,x,y)
        ans+=w

print(ans)