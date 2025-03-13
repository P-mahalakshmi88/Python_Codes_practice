# Mario and Bullet
# cook your dish here
t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    s = y // x 
    r = z - s
    if r > 0:
        print(r)
    else:
        print(0)