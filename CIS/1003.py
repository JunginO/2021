def fibo(inwon):
    result=[]
    a,b=0,1
    while a<inwon:
        result.append(a)
        a,b=b,a+b
    return result


ans=0
inwon=int(input())
fib=[]
fib=fibo(inwon)
n=len(fib)-1
b=True
for i in range(n):
    if fib[i]==inwon:
        ans=fib[i-1]
        b=False
        break
while b:
    for k in range(n):
        if inwon>=fib[n-k]:
            inwon-=fib[n-k]
            ans+=fib[n-k-1]
            k+=1

        if inwon==0:
            b=False
            break

            
if b==False:
    print(ans)
