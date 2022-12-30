# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    x = list(map(int, input().split()))  
    x.sort()
    print(x[len(x)-1])
        