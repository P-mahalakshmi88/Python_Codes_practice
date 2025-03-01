# Test Score
# cook your dish here
t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    if y % x == 0 and y <= n * x:
        print("YES")
    else:
        print("NO")