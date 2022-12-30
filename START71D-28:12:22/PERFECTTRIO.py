# cook your dish here
t=int(input())
for i in range(t):
 a,b,c=map(int,input().split())
 if (c==a+b):
    print("Yes")
 elif b==a+c:
    print("Yes")
 elif a==b+c:
    print("Yes")
 else:
    print("No")