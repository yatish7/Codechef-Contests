# cook your dish here
T=int(input())
for i in range(T):
     n=int(input())
     l=list(map(int,input().split()))
     c1=c2=0
     for i in range(n):
         if l[i]%2==0:
             c1+=1
         else:
             c2+=1
             
     if c2%2==0 and c2!=0:
        print("Yes")
     else:
        print("No")