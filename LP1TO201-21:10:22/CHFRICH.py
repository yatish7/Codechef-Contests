# cook your dish here
T=int(input())
for i in range(T):
    a,b,x=map(int,input().split())
    c=(b-a)//x
    print(c)