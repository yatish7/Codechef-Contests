# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    c=2**x
    a=c
    for i in range(n):
        a=a//2
        c=c-a
    print(c)