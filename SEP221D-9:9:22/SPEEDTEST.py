# cook your dish here
T=int(input())
for i in range(T):
    a,b,x,y=map(int,input().split())
    c=a/x
    d=b/y
    if c>d:
        print("ALICE")
    elif c<d:
        print("BOB")
    else:
        print("EQUAL")
        