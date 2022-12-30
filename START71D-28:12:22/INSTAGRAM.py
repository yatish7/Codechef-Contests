# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(10*y<x):
        print("Yes")
    else:
        print("No")