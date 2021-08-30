n=int(input())
counter=-1#카운트가 000부터시작

for i in range(10):
    for j in range(10):
        for k in range(10):
            if (((i*100)+(j*10)+k)<=n):
                if (j==(i+k)/2) or  (i==0 or (i==0 and j==0)):
                    counter+=1

print(counter)