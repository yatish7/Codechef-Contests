# cook your dish here
T=int(input())
for i in range(T):
    w,x,y,z=map(int,input().split())
    if (x==w or y==w or z==w or x+y==w or y+z==w or x+z==w or x+y+z==w):
        print("YES")
    else:
        print("NO")