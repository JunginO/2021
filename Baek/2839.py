n=int(input())
total=0
b=True
m=n//5
if (n-5*m)%3==0:
    pass
else:
    while (n-5*m)%3!=0:
        m-=1
        if(m<0):
            b=False
            break


if b:

    total=m+((n-5*m)//3)
    print(total)
else:
    print(-1)
