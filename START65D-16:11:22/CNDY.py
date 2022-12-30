# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    l=[]
    for i in range(2*n):
        if a.count(a[i])>2:
            print("No")
            break
    else:
        print("Yes")