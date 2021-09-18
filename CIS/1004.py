hp=int(input())
n=int(input())
weapons=[]
tmp=[]
counter=0


for _ in range(n):
    weapons.append(list(map(int, input().split())))

lgh=len(weapons)-1

for j in range(lgh):
    for i in range(lgh-j):
        if weapons[i]>weapons[i+1]:
            tmp=weapons[i]
            weapons[i]=weapons[i+1]
            weapons[i+1]=tmp

print(lgh,weapons)
for i in range(lgh):
    print(weapons[lgh-i])
    while ((weapons[lgh-i][1]>0)and hp>=0):
        weapons[lgh-i][1]-=1
        hp-=weapons[lgh-i][0]
        counter+=1
        print(weapons[lgh-i][1] , hp)
   

print(counter)

