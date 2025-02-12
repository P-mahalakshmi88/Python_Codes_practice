# Chef and NextGen
t = int(input())
for _ in range(t):
    a,b,x,y = map(int,input().split())
    r = a*b
    s = x*y
    if (s >= r):
        print("Yes")
    else:
        print("No")