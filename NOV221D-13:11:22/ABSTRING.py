# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    s=input()
    if n%2!=0:
        print("NO")
    else:
     l=[]
     for char in s:
        l.append(char)
     l.sort()
     s1=""
     s2=""
     for i in range(len(l)):
        if i%2==0:
            s1=s1+l[i]
        else:
            s2=s2+l[i]
     if s1==s2:
        print("YES")
     else:
        print("NO")
        