# cook your dish here
T=int(input())
for i in range(T):
    a,b,x,y=map(int,input().split())
    if a==b:
        print("YES")
    else:
        if a>b:
            if a-b<=y:
                print("YES")
            else:
                print("NO")
        else:
            if b-a<=x:
                 print("YES")
            else:
                print("NO")