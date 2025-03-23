# Chessboard Distance

t = int(input())
for _ in range(t):
    x , a, y, b = map(int,input().split())
    r = abs(x - y)
    s = abs(a - b)
    print(max(r,s))