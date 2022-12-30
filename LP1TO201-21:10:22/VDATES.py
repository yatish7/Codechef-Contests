# cook your dish here
T=int(input())
for i in range(T):
    d,l,r=map(int,input().split())
    if l<=d<=r:
        print("Take second dose now")
    elif d<l:
        print("Too Early")
    elif d>r:
        print("Too Late")
        