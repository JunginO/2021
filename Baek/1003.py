t=int(input())#테스트케이스 갯수
zero=[1,0,1]
one=[0,1,1]

def fibo(num):
    length=len(zero)
    if num>=length:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num],one[num])


for i in range(t):

    n=int(input())
    fibo(n)