# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    s=input()
    s1=""
    s2=""
    for i in range(1,len(s)+1):
        if i<=n/2:
            s1=s1+s[i-1]
        else:
            s2=s2+s[i-1]
    if s1==s2:
        print("YES")
    else:
        print("NO")