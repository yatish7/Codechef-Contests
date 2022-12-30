# cook your dish here
T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    c=a+b
    d=0
    for i in range(1,c+1):
        if c%i==0:
            d+=1
    if d==2:
        print("Alice")
    else:
        print("Bob")