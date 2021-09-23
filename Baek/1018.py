n,m=map(int,input().split())
il,ans=[],[]
for _ in range(n):
    tmpl=list(input())
    il.append(tmpl)

for i in range(n-7):
    for j in range(m-7):
        wcnt,bcnt=0,0
        for k in range(i,i+8):
            for p in range(j,j+8):
                if (k+p) %2== 0:
                    if il[k][p] != 'W':
                        wcnt +=1
                    if il[k][p] != 'B':
                        bcnt +=1
                else:
                    if il[k][p] != 'B':
                        wcnt +=1
                    if il[k][p] != 'W':
                        bcnt +=1
        ans.append(wcnt)
        ans.append(bcnt)
print(min(ans))
