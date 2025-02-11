#Expert Setter

T = int(input())
for _ in range(T):
    x , y = map(int,input().split())
    z = (y / x) * 100
    if z >= 50:
        print("YES")
    else:
        print("NO")