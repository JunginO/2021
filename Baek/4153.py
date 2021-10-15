while(True):
    lst=[0,0,0]
    lst[0],lst[1],lst[2]=map(int,input().split())
    lst.sort()
    if(sum(lst)==0):
        break

    if(((lst[0])**2+(lst[1])**2)==(lst[2])**2):
        print("right")
    else:
        print("wrong")
    
