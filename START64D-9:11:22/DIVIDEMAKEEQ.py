# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    a= list(map(int, input().split()))  
    a.sort()
    c=0
    for i in range(1,n):
        if a[i]%a[0]!=0:
            c=-1
            break
        elif a[i]%a[0]==0 and a[0]==a[i]:
            continue
        elif a[i]%a[0]==0:
            c+=1
    if c>=0:
        print(c)
    else:
        print(n)
            
            