# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    l=[]
    for i in range(n):
        if a[i]!=0 and b[i]!=0:
            c+=1
            l.append(c)
        elif a[i]==0 or b[i]==0:
            c=0
            l.append(0)
    l.sort()
    print(l[len(l)-1])