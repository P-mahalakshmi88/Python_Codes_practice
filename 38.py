# Bath in Winters

t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    z = y * 2
    s = x // z
    if z > x :
        print(0)
    else:
        print(s)
        