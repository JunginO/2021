n=int(input())
a=[]
for i in range(n):
    word=input()
    a.append(word)
a=set(a)
a=list(a)
a.sort()
a.sort(key=len, reverse=False)
for i in a:
    print(i)