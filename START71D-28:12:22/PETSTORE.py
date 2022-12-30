# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=[]
    if n%2!=0:
        print("No")
    else:
        a.sort()
        for i in range(n):
            if i%2==0:
                b.append(a[i])
            else:
                c.append(a[i])
        if b==c:
            print("Yes")
        else:
            print("No")
        