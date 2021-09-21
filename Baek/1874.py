n=int(input())
stack=[]
lastn=1
ans=[]
b=True
for _ in range(n):
    a=int(input())
    while a>=lastn:
        stack.append(lastn)
        ans.append('+')
        lastn+=1

    if stack[-1]==a:
        stack.pop()
        ans.append('-')
    else:
        b=False
        
if b==False:
    print('NO')
else:
    for i in ans:
        print(i)
