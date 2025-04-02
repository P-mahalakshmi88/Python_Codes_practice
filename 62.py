# Cup Finals

t = int(input())
for _ in range(t):
    x,y,d = map(int,input().split())
    z = abs(x - y) 
    if z <= d:
        print("YES")
    else:
        print("NO")