# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if (A+B)/2>C:
        print("YES")
    else:
        print("NO")