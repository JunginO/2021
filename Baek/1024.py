n,l=map(int, input().split())
S_l,y=0,0
x=-1
"""n=x*l+S_(l-1)
x*l=n-(l-1)(l)/2
"""

for length in range(l,101):
    S_l=((length-1)*length)/2
    if (n-S_l)%length==0 and (n-S_l)//length>=0:
        x=(n-S_l)//length
        y=length
        break
    
x=int(x)
if(x==-1):
    print(-1)
else:
    for i in range(x,x+y):
        print(i,end=" ")

