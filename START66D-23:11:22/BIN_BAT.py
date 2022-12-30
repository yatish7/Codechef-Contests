# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    c=0
    n=n/2
    while(n!=1):
        c=c+a+b
        n=n/2
    else:
        c+=a
    print(c)