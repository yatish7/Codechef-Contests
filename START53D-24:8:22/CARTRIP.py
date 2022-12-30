# cook your code here
T=int(input())
for i in range(T):
    n=int(input())
    if n<=300:
        print(300*10)
    else:
        print(300*10+(n-300)*10)