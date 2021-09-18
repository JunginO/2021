hp=int(input())
n=int(input())
weapons=[]
counter=0

for _ in range(n):
    weapons.append(list(map(int, input().split())))

lgh=len(weapons)-1

for j in range(lgh):
    for i in range(lgh-j):
        if weapons[i]>weapons[i+1]:
            weapons[i],weapons[i+1]=weapons[i+1],weapons[i]

for i in range(lgh+1):
    if hp<0:
        break
    while ((weapons[lgh-i][1]>0)):
        
        weapons[lgh-i][1]-=1
        hp-=weapons[lgh-i][0]
        counter+=1
        if hp<=0:
            break

print(counter)

