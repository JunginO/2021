"""n=int(input())
flag=True
def sosu(n):
    for i in range(2,n):
        if n%i==0:
            global flag
            flag=False
            break
sosu(n)
if flag:
    print(1)
else:
    print(0)
    
    
    𝑚𝑜𝑑 𝑛 어떤 정수 a를 n로 나눈 나머지만을 보겠다는 것
    𝒂^𝒅≠𝟏 (𝒎𝒐𝒅 𝒏)
    𝒂^(𝒅×𝟐^𝒓 )≠−𝟏 (𝒎𝒐𝒅 𝒏)           
     𝒇𝒐𝒓 𝒂𝒍𝒍 𝟎≤𝒓≤𝒔−𝟏

    동시 만족시 합성수  
    """
def nanum(n):
    global cnt
    if (n)%2==0:
        cnt+=1
        return nanum((n)//2)
    else:
        return cnt
n=int(input())
k=n-1
cnt=0
s=nanum(k)
d=(n-1)//pow(2,s)
lst=[2,7,61]
for i in lst:
    if pow(i,d,n)!=1:
        result=True
    else:
        result=False
    for r in range(s):
        if (pow(i,d*pow(2,r),n))!=(n-1):
            result=result*True
        else:
            result=result*False
    if result==False:
        break
if result==False:
    print(1)
else:
    print(0)
