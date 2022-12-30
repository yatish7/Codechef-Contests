# cook your dish here
t=int(input())
for i in range(t):
    a,c=map(int,input().split())
    if (a%2==0 and c%2==0) or (a%2!=0 and c%2!=0):
        print((a+c)//2)
    else:
        print(-1)
